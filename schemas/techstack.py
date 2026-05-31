import pydantic
import typing
import enum


class ExpectedScale(str, enum.Enum):
    small = "Small — under 1000 users"
    medium = "Medium — 1000 to 50000 users"
    large = "Large — 50000 plus users"
    no_preference = "No Preference"


class BudgetConstraints(str, enum.Enum):
    low = "Low — prefer free and open source tools"
    medium = "Medium — some paid services acceptable"
    high = "High — cost is not a concern"
    no_preference = "No Preference"


class DeploymentTarget(str, enum.Enum):
    aws = "AWS"
    google_cloud = "Google Cloud"
    azure = "Azure"
    vercel = "Vercel"
    digital_ocean = "DigitalOcean"
    no_preference = "No Preference"


class TechStackInput(pydantic.BaseModel):
    project_description: str = pydantic.Field(
        ...,
        description="The project description explaining the purpose, features, and goals of the project",
    )
    project_roadmap: str = pydantic.Field(
        ...,
        description="The full project roadmap including all phases, milestones, and deliverables",
    )
    team_size: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Team size and experience level e.g. 3 developers comfortable with JavaScript and Python",
    )
    expected_scale: typing.Optional[ExpectedScale] = pydantic.Field(
        default=ExpectedScale.no_preference,
        description="Expected scale of the project — Small, Medium, Large, or No Preference",
    )
    preferred_languages: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Preferred programming languages e.g. Python for backend, JavaScript for frontend",
    )
    budget_constraints: typing.Optional[BudgetConstraints] = pydantic.Field(
        default=BudgetConstraints.no_preference,
        description="Budget constraints — Low, Medium, High, or No Preference",
    )
    deployment_target: typing.Optional[DeploymentTarget] = pydantic.Field(
        default=DeploymentTarget.no_preference,
        description="Preferred deployment target — AWS, Google Cloud, Azure, Vercel, DigitalOcean, or No Preference",
    )
    additional_notes: typing.Optional[str] = pydantic.Field(
        default=None,
        description="Any extra instructions, constraints, or special requirements for the tech stack suggestion",
    )
