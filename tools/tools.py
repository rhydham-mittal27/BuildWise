import prompts
import langchain_community.tools
import chains


@langchain_community.tools.tool
def create_roadmap(query):
    """
    Creates a detailed software development roadmap from a user's project idea.

    Use this tool when the user wants to:
    - Build a new software project, startup, website, mobile app, SaaS, AI product, or platform.
    - Get a step-by-step implementation plan.
    - Break a project into phases, milestones, and deliverables.
    - Understand how to start building a project.

    Input:
    - A natural language description of the project.

    Output:
    - A structured development roadmap including project phases, milestones,
      deliverables, recommended implementation order, and timeline estimates.
    """
    return chains.tool_chain(query, prompts.RoadmapPPs())


@langchain_community.tools.tool
def generate_database_schema(query):
    """
    Generates a complete database schema for a software project based on
    project requirements, features, and business logic.

    Use this tool when the user wants to:
    - Design a database for a project.
    - Generate tables, relationships, and entities.
    - Create a PostgreSQL, MySQL, or SQL database structure.
    - Understand how data should be organized for a software application.
    - Convert project requirements into a database design.

    The generated schema may include:
    - Tables and columns
    - Primary and foreign keys
    - Relationships between entities
    - Constraints and indexes
    - Data modeling recommendations

    Args:
        query: A description of the project, roadmap, features, or
        requirements for which a database schema should be generated.

    Returns:
        A detailed database schema including tables, attributes,
        relationships, and database design recommendations.
    """
    return chains.tool_chain(query, prompts.DatabaseGenPPs())


@langchain_community.tools.tool
def generate_api_plan(query):
    """
    Generates a complete backend API architecture for a software project.

    Use this tool when the user wants to:
    - Design REST APIs.
    - Create FastAPI, Express.js, or backend endpoints.
    - Generate API routes and request/response structures.
    - Plan backend architecture.
    - Define authentication and authorization flows.

    The generated plan may include:
    - API endpoints
    - Request and response schemas
    - Authentication flows
    - Role-based access control
    - Service architecture
    - Validation requirements

    Args:
        query: Project requirements, roadmap, or database schema.

    Returns:
        A complete API design and backend architecture plan.
    """
    return chains.tool_chain(query, prompts.APIGenPPs())


@langchain_community.tools.tool
def generate_frontend_plan(query):
    """
    Generates a complete frontend architecture and UI implementation plan.

    Use this tool when the user wants to:
    - Design the frontend of an application.
    - Create page and screen structures.
    - Plan React, Next.js, React Native, or Flutter applications.
    - Design user flows and navigation.
    - Generate component architecture.

    The generated plan may include:
    - Pages and screens
    - User flows
    - Component hierarchy
    - State management recommendations
    - API integration points
    - Folder structure

    Args:
        query: Project requirements, roadmap, database schema, or API plan.

    Returns:
        A detailed frontend architecture and implementation plan.
    """
    return chains.tool_chain(query, prompts.FrontendGenPPs())


@langchain_community.tools.tool
def generate_task(query):
    """
    Generates a detailed implementation task breakdown for a software project.

    Use this tool when the user wants to:
    - Break a project into actionable development tasks.
    - Create an implementation plan from a roadmap.
    - Generate sprint-wise work items.
    - Identify what should be built first.
    - Convert architecture and requirements into executable tasks.
    - Create a development backlog for a team or individual developer.

    The generated task plan may include:
    - Project phases
    - Sprint planning
    - Backend tasks
    - Frontend tasks
    - Database tasks
    - Infrastructure tasks
    - Testing tasks
    - Deployment tasks
    - Task dependencies
    - Recommended implementation order

    Args:
        query: Project requirements, roadmap, database schema,
        API plan, frontend plan, or any combination of project
        artifacts from which implementation tasks should be generated.

    Returns:
        A structured task breakdown containing actionable development
        tasks, priorities, dependencies, and recommended execution order.
    """
    return chains.tool_chain(query, prompts.TaskGenPPs())


@langchain_community.tools.tool
def suggest_stack(query):
    """
    Recommends an appropriate technology stack for a software project.

    Use this tool when the user wants:
    - Technology recommendations.
    - Framework selection.
    - Database recommendations.
    - Infrastructure recommendations.
    - Deployment suggestions.

    Returns:
    - Frontend stack
    - Backend stack
    - Database
    - Infrastructure
    - Deployment strategy
    - Tradeoffs and rationale
    """
    return chains.tool_chain(query, prompts.SuggestStackPPs())


@langchain_community.tools.tool
def ask_questions_for_context(query):
    """
        Analyzes a project idea and identifies missing or unclear information
        required for accurate software planning and architecture generation.

        Use this tool when the user provides an incomplete, ambiguous, or
        high-level project description and additional context is needed before
        generating project artifacts.

        The tool may:
        - Identify missing requirements.
        - Detect ambiguous project details.
        - Generate clarifying questions.
        - Highlight assumptions that would otherwise need to be made.
        - Collect information needed for roadmap generation.
        - Improve the quality of subsequent planning and architecture outputs.

        Typical areas of clarification include:
        - Target audience
        - Platform (Web, Mobile, Desktop)
        - Core features
        - User roles
        - Authentication requirements
        - Scalability expectations
        - Budget constraints
        - Timeline expectations
        - Technical preferences

        The tool should generate all important clarification questions in a
        single response whenever possible to minimize back-and-forth exchanges.
    Use this tool FIRST when:
    - The project description is less than 3-4 sentences.
    - Important requirements are missing.
    - The target audience is unclear.
    - The platform (web/mobile/desktop) is unclear.
    - Core features are not sufficiently specified.

    This tool should generally be called before roadmap generation
    whenever assumptions would otherwise be required.
        Args:
            query: A project idea, feature request, startup concept, or software
            description that may require additional context before planning.

        Returns:
            A structured list of clarification questions and missing
            requirements needed to better understand the project.
    """
    return chains.tool_chain(query, prompts.AskForContextPPs())
