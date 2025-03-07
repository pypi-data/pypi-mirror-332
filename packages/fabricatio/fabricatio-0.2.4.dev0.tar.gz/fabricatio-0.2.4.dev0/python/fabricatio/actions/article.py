"""Actions for transmitting tasks to targets."""

from os import PathLike
from pathlib import Path
from typing import Callable, List

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict

from fabricatio.journal import logger
from fabricatio.models.action import Action
from fabricatio.models.generic import ProposedAble
from fabricatio.models.task import Task


class Equation(BaseModel):
    """Structured representation of mathematical equations (including their physical or conceptual meanings)."""

    model_config = ConfigDict(use_attribute_docstrings=True)

    description: str = Field(...)
    """A concise explanation of the equation's meaning, purpose, and relevance in the context of the research."""

    latex_code: str = Field(...)
    """The LaTeX code used to represent the equation in a publication-ready format."""


class Figure(BaseModel):
    """Structured representation of figures (including their academic significance and explanatory captions)."""

    model_config = ConfigDict(use_attribute_docstrings=True)

    description: str = Field(...)
    """A detailed explanation of the figure's content and its role in conveying key insights."""

    figure_caption: str = Field(...)
    """The caption accompanying the figure, summarizing its main points and academic value."""


class ArticleEssence(ProposedAble):
    """Structured representation of the core elements of an academic paper(providing a comprehensive digital profile of the paper's essential information)."""

    # Basic Metadata
    title: str = Field(...)
    """The full title of the paper, including any subtitles if applicable."""

    authors: List[str] = Field(default_factory=list)
    """A list of the paper's authors, typically in the order of contribution."""

    keywords: List[str] = Field(default_factory=list)
    """A list of keywords that summarize the paper's focus and facilitate indexing."""

    publication_year: int = Field(None)
    """The year in which the paper was published."""

    # Core Content Elements
    domain: List[str] = Field(default_factory=list)
    """The research domains or fields addressed by the paper (e.g., ['Natural Language Processing', 'Computer Vision'])."""

    abstract: str = Field(...)
    """A structured abstract that outlines the research problem, methodology, and conclusions in three distinct sections."""

    core_contributions: List[str] = Field(default_factory=list)
    """Key academic contributions that distinguish the paper from prior work in the field."""

    technical_novelty: List[str] = Field(default_factory=list)
    """Specific technical innovations introduced by the research, listed as individual points."""

    # Academic Achievements Showcase
    highlighted_equations: List[Equation] = Field(default_factory=list)
    """Core mathematical equations that represent breakthroughs in the field, accompanied by explanations of their physical or conceptual significance."""

    highlighted_algorithms: List[str] = Field(default_factory=list)
    """Pseudocode for key algorithms, annotated to highlight innovative components."""

    highlighted_figures: List[Figure] = Field(default_factory=list)
    """Critical diagrams or illustrations, each accompanied by a caption explaining their academic importance."""

    highlighted_tables: List[str] = Field(default_factory=list)
    """Important data tables, annotated to indicate statistical significance or other notable findings."""

    # Academic Discussion Dimensions
    research_problem: str = Field("")
    """A clearly defined research question or problem addressed by the study."""

    limitations: List[str] = Field(default_factory=list)
    """An analysis of the methodological or experimental limitations of the research."""

    future_work: List[str] = Field(default_factory=list)
    """Suggestions for potential directions or topics for follow-up studies."""

    impact_analysis: str = Field("")
    """An assessment of the paper's potential influence on the development of the field."""


class ExtractArticleEssence(Action):
    """Extract the essence of article(s)."""

    name: str = "extract article essence"
    """The name of the action."""
    description: str = "Extract the essence of an article. output as json"
    """The description of the action."""

    output_key: str = "article_essence"
    """The key of the output data."""

    async def _execute[P: PathLike | str](
        self,
        task_input: Task,
        reader: Callable[[P], str] = lambda p: Path(p).read_text(encoding="utf-8"),
        **_,
    ) -> List[ArticleEssence]:
        if not await self.ajudge(
            f"= Task\n{task_input.briefing}\n\n\n= Role\n{self.briefing}",
            affirm_case="The task does not violate the role, and could be approved since the file dependencies are specified.",
            deny_case="The task does violate the role, and could not be approved.",
        ):
            logger.info(err := "Task not approved.")
            raise RuntimeError(err)

        # trim the references
        contents = ["References".join(c.split("References")[:-1]) for c in map(reader, task_input.dependencies)]
        return await self.propose(
            ArticleEssence,
            contents,
            system_message=f"# your personal briefing: \n{self.briefing}",
        )
