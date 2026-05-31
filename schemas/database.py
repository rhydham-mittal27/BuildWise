import enum
import pydantic
import typing


class InputType(str, enum.Enum):
    project_description = "Project Description"
    project_roadmap = "Project Roadmap"


class DatabaseType(str, enum.Enum):
    relational = "Relational"
    non_relational = "Non-Relational"
    no_preference = "No Preference"


class DatabaseSchemaInput(pydantic.BaseModel):
    input_type: InputType
    content: str

    database_type: typing.Optional[DatabaseType] = DatabaseType.no_preference

    additional_notes: typing.Optional[str] = None
