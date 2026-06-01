# schemas.py

import pydantic
import typing


class ClarificationTurn(pydantic.BaseModel):
    question: str = pydantic.Field(description="Question previously asked to the user.")

    answer: str = pydantic.Field(description="User's answer to the question.")


class AskForContextInput(pydantic.BaseModel):
    """
    Input passed to the ask_questions_for_context tool.
    Contains original project description plus all previous
    clarification rounds.
    """

    project_description: str = pydantic.Field(
        description=(
            "Original project description extracted from the first user request."
        )
    )

    clarification_history: list[ClarificationTurn] = pydantic.Field(
        default_factory=list,
        description=("All previous clarification questions and user answers."),
    )


class AskForContextOutput(pydantic.BaseModel):
    """
    Output from the ask_questions_for_context tool.
    """

    is_sufficient: bool = pydantic.Field(
        description=("True if enough context exists to generate project artifacts.")
    )

    missing_info: typing.Optional[list[str]] = pydantic.Field(
        default=None, description="Information still missing."
    )

    questions: typing.Optional[list[str]] = pydantic.Field(
        default=None, description="Clarifying questions to ask next."
    )
