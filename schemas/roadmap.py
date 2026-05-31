import pydantic
import typing


class ProjectRoadmapInput(pydantic.BaseModel):
    project_title: str = pydantic.Field(...)
    project_description: str = pydantic.Field(...)
    target_audience: str = pydantic.Field(...)
    desired_outcome: str = pydantic.Field(...)

    resources: typing.Optional[str] = pydantic.Field(default=None)

    timeline: typing.Optional[str] = pydantic.Field(default=None)
