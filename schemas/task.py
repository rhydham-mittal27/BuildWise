import pydantic
import typing
import enum


class SprintDuration(str, enum.Enum):
    one_week = "1 Week"
    two_weeks = "2 Weeks"
    three_weeks = "3 Weeks"
    no_preference = "No Preference"


class TaskGenerationInput(pydantic.BaseModel):
    project_roadmap: str = pydantic.Field(
        ...,
        description="The full project roadmap including all phases, milestones, and deliverables",
    )
    database_schema: str = pydantic.Field(
        ...,
        description="The database schema including tables, fields, relationships, and constraints",
    )
    api_plan: str = pydantic.Field(
        ...,
        description="The API plan including all route groups, endpoints, request and response structures",
    )
    frontend_plan: str = pydantic.Field(
        ...,
        description="The frontend plan including all pages, routes, components, and state management strategy",
    )
    phase_or_week: str = pydantic.Field(
        ...,
        description="The specific phase or week to generate tasks for e.g. Phase 1, Week 2, Sprint 3, User Authentication Phase",
    )
    team_composition: typing.Optional[str] = pydantic.Field(
        default=None,
        description="The team composition for the phase e.g. 2 backend developers, 1 frontend developer, 1 QA engineer",
    )
    sprint_duration: typing.Optional[SprintDuration] = pydantic.Field(
        default=SprintDuration.no_preference,
        description="The duration of the sprint — 1 Week, 2 Weeks, 3 Weeks, or No Preference",
    )
    additional_notes: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Any extra instructions, constraints, or special requirements for the task generation",
    )
