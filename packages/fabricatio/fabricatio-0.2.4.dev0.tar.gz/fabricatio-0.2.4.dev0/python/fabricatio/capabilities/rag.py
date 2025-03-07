"""A module for the RAG (Retrieval Augmented Generation) model."""

try:
    from pymilvus import MilvusClient
except ImportError as e:
    raise RuntimeError("pymilvus is not installed. Have you installed `fabricatio[rag]` instead of `fabricatio`") from e
from functools import lru_cache
from operator import itemgetter
from os import PathLike
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Self, Union, Unpack, overload

from fabricatio._rust_instances import template_manager
from fabricatio.config import configs
from fabricatio.journal import logger
from fabricatio.models.kwargs_types import CollectionSimpleConfigKwargs, EmbeddingKwargs, FetchKwargs, LLMKwargs
from fabricatio.models.usages import EmbeddingUsage
from fabricatio.models.utils import MilvusData
from more_itertools.recipes import flatten
from pydantic import Field, PrivateAttr


@lru_cache(maxsize=None)
def create_client(uri: str, token: str = "", timeout: Optional[float] = None) -> MilvusClient:
    """Create a Milvus client."""
    return MilvusClient(
        uri=uri,
        token=token,
        timeout=timeout,
    )


class RAG(EmbeddingUsage):
    """A class representing the RAG (Retrieval Augmented Generation) model."""

    target_collection: Optional[str] = Field(default=None)
    """The name of the collection being viewed."""

    _client: Optional[MilvusClient] = PrivateAttr(None)
    """The Milvus client used for the RAG model."""

    @property
    def client(self) -> MilvusClient:
        """Return the Milvus client."""
        if self._client is None:
            raise RuntimeError("Client is not initialized. Have you called `self.init_client()`?")
        return self._client

    def init_client(
        self,
        milvus_uri: Optional[str] = None,
        milvus_token: Optional[str] = None,
        milvus_timeout: Optional[float] = None,
    ) -> Self:
        """Initialize the Milvus client."""
        self._client = create_client(
            uri=milvus_uri or (self.milvus_uri or configs.rag.milvus_uri).unicode_string(),
            token=milvus_token
            or (token.get_secret_value() if (token := (self.milvus_token or configs.rag.milvus_token)) else ""),
            timeout=milvus_timeout or self.milvus_timeout,
        )
        return self

    @overload
    async def pack(
        self, input_text: List[str], subject: Optional[str] = None, **kwargs: Unpack[EmbeddingKwargs]
    ) -> List[MilvusData]: ...
    @overload
    async def pack(
        self, input_text: str, subject: Optional[str] = None, **kwargs: Unpack[EmbeddingKwargs]
    ) -> MilvusData: ...

    async def pack(
        self, input_text: List[str] | str, subject: Optional[str] = None, **kwargs: Unpack[EmbeddingKwargs]
    ) -> List[MilvusData] | MilvusData:
        """Asynchronously generates MilvusData objects for the given input text.

        Args:
            input_text (List[str] | str): A string or list of strings to generate embeddings for.
            subject (Optional[str]): The subject of the input text. Defaults to None.
            **kwargs (Unpack[EmbeddingKwargs]): Additional keyword arguments for embedding.

        Returns:
            List[MilvusData] | MilvusData: The generated MilvusData objects.
        """
        if isinstance(input_text, str):
            return MilvusData(vector=await self.vectorize(input_text, **kwargs), text=input_text, subject=subject)
        vecs = await self.vectorize(input_text, **kwargs)
        return [
            MilvusData(
                vector=vec,
                text=text,
                subject=subject,
            )
            for text, vec in zip(input_text, vecs, strict=True)
        ]

    def view(
        self, collection_name: Optional[str], create: bool = False, **kwargs: Unpack[CollectionSimpleConfigKwargs]
    ) -> Self:
        """View the specified collection.

        Args:
            collection_name (str): The name of the collection.
            create (bool): Whether to create the collection if it does not exist.
            **kwargs (Unpack[CollectionSimpleConfigKwargs]): Additional keyword arguments for collection configuration.
        """
        if create and collection_name and not self._client.has_collection(collection_name):
            kwargs["dimension"] = kwargs.get("dimension") or self.milvus_dimensions or configs.rag.milvus_dimensions
            self._client.create_collection(collection_name, auto_id=True, **kwargs)
            logger.info(f"Creating collection {collection_name}")

        self.target_collection = collection_name
        return self

    def quit_viewing(self) -> Self:
        """Quit the current view.

        Returns:
            Self: The current instance, allowing for method chaining.
        """
        return self.view(None)

    @property
    def safe_target_collection(self) -> str:
        """Get the name of the collection being viewed, raise an error if not viewing any collection.

        Returns:
            str: The name of the collection being viewed.
        """
        if self.target_collection is None:
            raise RuntimeError("No collection is being viewed. Have you called `self.view()`?")
        return self.target_collection

    def add_document[D: Union[Dict[str, Any], MilvusData]](
        self, data: D | List[D], collection_name: Optional[str] = None, flush: bool = False
    ) -> Self:
        """Adds a document to the specified collection.

        Args:
            data (Union[Dict[str, Any], MilvusData] | List[Union[Dict[str, Any], MilvusData]]): The data to be added to the collection.
            collection_name (Optional[str]): The name of the collection. If not provided, the currently viewed collection is used.
            flush (bool): Whether to flush the collection after insertion.

        Returns:
            Self: The current instance, allowing for method chaining.
        """
        if isinstance(data, MilvusData):
            data = data.prepare_insertion()
        if isinstance(data, list):
            data = [d.prepare_insertion() if isinstance(d, MilvusData) else d for d in data]
        c_name = collection_name or self.safe_target_collection
        self._client.insert(c_name, data)

        if flush:
            logger.debug(f"Flushing collection {c_name}")
            self._client.flush(c_name)
        return self

    async def consume_file(
        self,
        source: List[PathLike] | PathLike,
        reader: Callable[[PathLike], str] = lambda path: Path(path).read_text(encoding="utf-8"),
        collection_name: Optional[str] = None,
    ) -> Self:
        """Consume a file and add its content to the collection.

        Args:
            source (PathLike): The path to the file to be consumed.
            reader (Callable[[PathLike], MilvusData]): The reader function to read the file.
            collection_name (Optional[str]): The name of the collection. If not provided, the currently viewed collection is used.

        Returns:
            Self: The current instance, allowing for method chaining.
        """
        if not isinstance(source, list):
            source = [source]
        return await self.consume_string([reader(s) for s in source], collection_name)

    async def consume_string(self, text: List[str] | str, collection_name: Optional[str] = None) -> Self:
        """Consume a string and add it to the collection.

        Args:
            text (List[str] | str): The text to be added to the collection.
            collection_name (Optional[str]): The name of the collection. If not provided, the currently viewed collection is used.

        Returns:
            Self: The current instance, allowing for method chaining.
        """
        self.add_document(await self.pack(text), collection_name or self.safe_target_collection, flush=True)
        return self

    async def afetch_document(
        self,
        vecs: List[List[float]],
        desired_fields: List[str] | str,
        collection_name: Optional[str] = None,
        similarity_threshold: float = 0.37,
        result_per_query: int = 10,
    ) -> List[Dict[str, Any]] | List[Any]:
        """Fetch data from the collection.

        Args:
            vecs (List[List[float]]): The vectors to search for.
            desired_fields (List[str] | str): The fields to retrieve.
            collection_name (Optional[str]): The name of the collection. If not provided, the currently viewed collection is used.
            similarity_threshold (float): The threshold for similarity, only results above this threshold will be returned.
            result_per_query (int): The number of results to return per query.

        Returns:
            List[Dict[str, Any]] | List[Any]: The retrieved data.
        """
        # Step 1: Search for vectors
        search_results = self._client.search(
            collection_name or self.safe_target_collection,
            vecs,
            search_params={"radius": similarity_threshold},
            output_fields=desired_fields if isinstance(desired_fields, list) else [desired_fields],
            limit=result_per_query,
        )

        # Step 2: Flatten the search results
        flattened_results = flatten(search_results)

        # Step 3: Sort by distance (descending)
        sorted_results = sorted(flattened_results, key=itemgetter("distance"), reverse=True)

        logger.debug(f"Searched similarities: {[t['distance'] for t in sorted_results]}")
        # Step 4: Extract the entities
        resp = [result["entity"] for result in sorted_results]

        if isinstance(desired_fields, list):
            return resp
        return [r.get(desired_fields) for r in resp]

    async def aretrieve(
        self,
        query: List[str] | str,
        collection_name: Optional[str] = None,
        final_limit: int = 20,
        **kwargs: Unpack[FetchKwargs],
    ) -> List[str]:
        """Retrieve data from the collection.

        Args:
            query (List[str] | str): The query to be used for retrieval.
            collection_name (Optional[str]): The name of the collection. If not provided, the currently viewed collection is used.
            final_limit (int): The final limit on the number of results to return.
            **kwargs (Unpack[FetchKwargs]): Additional keyword arguments for retrieval.

        Returns:
            List[str]: A list of strings containing the retrieved data.
        """
        if isinstance(query, str):
            query = [query]
        return (
            await self.afetch_document(
                vecs=(await self.vectorize(query)),
                desired_fields="text",
                collection_name=collection_name,
                **kwargs,
            )
        )[:final_limit]

    async def aask_retrieved(
        self,
        question: str | List[str],
        query: List[str] | str,
        collection_name: Optional[str] = None,
        extra_system_message: str = "",
        result_per_query: int = 10,
        final_limit: int = 20,
        similarity_threshold: float = 0.37,
        **kwargs: Unpack[LLMKwargs],
    ) -> str:
        """Asks a question by retrieving relevant documents based on the provided query.

        This method performs document retrieval using the given query, then asks the
        specified question using the retrieved documents as context.

        Args:
            question (str | List[str]): The question or list of questions to be asked.
            query (List[str] | str): The query or list of queries used for document retrieval.
            collection_name (Optional[str]): The name of the collection to retrieve documents from.
                                              If not provided, the currently viewed collection is used.
            extra_system_message (str): An additional system message to be included in the prompt.
            result_per_query (int): The number of results to return per query. Default is 10.
            final_limit (int): The maximum number of retrieved documents to consider. Default is 20.
            similarity_threshold (float): The threshold for similarity, only results above this threshold will be returned.
            **kwargs (Unpack[LLMKwargs]): Additional keyword arguments passed to the underlying `aask` method.

        Returns:
            str: A string response generated after asking with the context of retrieved documents.
        """
        docs = await self.aretrieve(
            query,
            collection_name,
            final_limit,
            result_per_query=result_per_query,
            similarity_threshold=similarity_threshold,
        )

        rendered = template_manager.render_template(configs.templates.retrieved_display_template, {"docs": docs[::-1]})

        logger.debug(f"Retrieved Documents: \n{rendered}")
        return await self.aask(
            question,
            f"{rendered}\n\n{extra_system_message}",
            **kwargs,
        )
