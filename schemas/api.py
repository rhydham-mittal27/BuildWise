import enum
import pydantic
import typing


class ApiStyle(str, enum.Enum):
    rest = "REST"
    graphql = "GraphQL"
    no_preference = "No Preference"


class AuthMethod(str, enum.Enum):
    jwt = "JWT"
    oauth2 = "OAuth2"
    api_key = "API Key"
    session = "Session"
    no_preference = "No Preference"


class ApiPlanInput(pydantic.BaseModel):
    project_description: str
    database_schema: str

    api_style: typing.Optional[ApiStyle] = ApiStyle.no_preference

    auth_method: typing.Optional[AuthMethod] = AuthMethod.no_preference

    additional_notes: typing.Optional[str] = None
