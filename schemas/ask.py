import pydantic
import typing


class ProjectDiscoveryInput(pydantic.BaseModel):
    context_so_far: str = pydantic.Field(
        ...,
        description="The full conversation history so far including all questions asked and answers provided across all rounds",
    )
    final_project_context_summary: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The final structured summary of the project context generated at the closing round — null until the conversation is complete",
    )
