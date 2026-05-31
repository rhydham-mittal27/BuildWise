import enum
import pydantic
import typing


class FrontendFramework(str, enum.Enum):
    react = "React"
    nextjs = "Next.js"
    vuejs = "Vue.js"
    nuxtjs = "Nuxt.js"
    angular = "Angular"
    no_preference = "No Preference"


class StylingApproach(str, enum.Enum):
    tailwind = "Tailwind CSS"
    material_ui = "Material UI"
    chakra_ui = "Chakra UI"
    bootstrap = "Bootstrap"
    styled_components = "Styled Components"
    no_preference = "No Preference"


class StateManagement(str, enum.Enum):
    redux_toolkit = "Redux Toolkit"
    zustand = "Zustand"
    recoil = "Recoil"
    context_api = "Context API"
    no_preference = "No Preference"


class FrontendPlanInput(pydantic.BaseModel):
    project_description: str
    database_schema: str
    api_plan: str

    frontend_framework: typing.Optional[FrontendFramework] = (
        FrontendFramework.no_preference
    )

    styling_approach: typing.Optional[StylingApproach] = StylingApproach.no_preference

    state_management: typing.Optional[StateManagement] = StateManagement.no_preference

    additional_notes: typing.Optional[str] = None
