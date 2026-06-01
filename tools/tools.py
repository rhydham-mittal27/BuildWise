"""
tools.py

LangChain tool definitions for AI-powered software project planning.
Each tool wraps a chain call and is used by the agent to generate
project artifacts such as roadmaps, schemas, API plans, and tasks.
"""

import langchain_community.tools
import prompts
import chains


def _run_tool(query: str, prompt_params) -> str:
    """Shared error-handled wrapper around chains.tool_chain."""
    try:
        return chains.tool_chain(query, prompt_params)
    except Exception as e:
        return f"Error running tool: {str(e)}"


@langchain_community.tools.tool
def create_roadmap(query: str) -> str:
    """
    Creates a structured software development roadmap from a project idea.

    Use when the user wants to build a new project (app, SaaS, platform, website)
    and needs a step-by-step implementation plan with phases, milestones,
    deliverables, and timeline estimates.

    Args:
        query: A natural language description of the project idea.

    Returns:
        A structured development roadmap with phases, milestones,
        deliverables, implementation order, and timeline estimates.
    """
    return _run_tool(query, prompts.RoadmapPPs())


@langchain_community.tools.tool
def generate_database_schema(query: str) -> str:
    """
    Generates a complete database schema based on project requirements.

    Use when the user wants to design a database, generate tables/relationships,
    or convert project requirements into a data model (PostgreSQL, MySQL, etc.).

    Args:
        query: A description of the project features, requirements, or roadmap.

    Returns:
        A detailed database schema with tables, columns, primary/foreign keys,
        relationships, constraints, indexes, and modeling recommendations.
    """
    return _run_tool(query, prompts.DatabaseGenPPs())


@langchain_community.tools.tool
def generate_api_plan(query: str) -> str:
    """
    Generates a backend API architecture for a software project.

    Use when the user wants to design REST APIs, plan backend endpoints
    (FastAPI, Express.js, etc.), or define authentication and authorization flows.

    Args:
        query: Project requirements, roadmap, or database schema.

    Returns:
        A complete API design including endpoints, request/response schemas,
        authentication flows, RBAC, service architecture, and validation rules.
    """
    return _run_tool(query, prompts.APIGenPPs())


@langchain_community.tools.tool
def generate_frontend_plan(query: str) -> str:
    """
    Generates a frontend architecture and UI implementation plan.

    Use when the user wants to design a frontend (React, Next.js, React Native,
    Flutter), plan page/screen structures, user flows, or component hierarchy.

    Args:
        query: Project requirements, roadmap, database schema, or API plan.

    Returns:
        A detailed frontend plan including pages, user flows, component
        hierarchy, state management, API integration points, and folder structure.
    """
    return _run_tool(query, prompts.FrontendGenPPs())


@langchain_community.tools.tool
def generate_task(query: str) -> str:
    """
    Generates a detailed, sprint-wise implementation task breakdown.

    Use when the user wants to convert a roadmap or architecture into
    actionable development tasks, a backlog, or a sprint plan.

    Args:
        query: Project requirements, roadmap, schema, API plan, frontend plan,
               or any combination of project artifacts.

    Returns:
        A structured task breakdown with phases, backend/frontend/infra/testing
        tasks, priorities, dependencies, and recommended execution order.
    """
    return _run_tool(query, prompts.TaskGenPPs())


@langchain_community.tools.tool
def suggest_stack(query: str) -> str:
    """
    Recommends a technology stack for a software project.

    Use when the user wants technology, framework, database, infrastructure,
    or deployment recommendations with rationale and tradeoff analysis.

    Args:
        query: A description of the project requirements or constraints.

    Returns:
        Stack recommendations for frontend, backend, database, infrastructure,
        and deployment, along with tradeoffs and reasoning.
    """
    return _run_tool(query, prompts.SuggestStackPPs())


@langchain_community.tools.tool
def ask_questions_for_context(query: str) -> str:
    """
    Identifies missing information and generates clarifying questions.

    Use this tool FIRST when the project description is vague, incomplete,
    or fewer than 3-4 sentences. Call before roadmap or schema generation
    to avoid making assumptions.

    Covers gaps in: target audience, platform (web/mobile/desktop), core
    features, user roles, auth requirements, scalability, budget, and timeline.

    Args:
        query: A project idea or description that may need clarification.

    Returns:
        A structured list of clarifying questions and missing requirements.
    """
    print(query) 
    return _run_tool(query, prompts.AskForContextPPs())
