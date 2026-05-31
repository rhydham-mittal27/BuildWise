import langchain_core.prompts
import schemas
import langchain_core.output_parsers


class RoadmapPPs:
    def __init__(self) -> None:
        self.prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
            You are an expert project strategist and technical architect with deep experience in software development, product management, and agile methodologies. Your role is to analyze a project idea and generate a clear, structured, and actionable project roadmap.
        When given a project description or idea brief, you will produce a roadmap that includes:

        Project Overview - A concise summary of the project goal and vision
        Key Milestones - Major phases broken down in logical order
        Tasks & Deliverables - Specific tasks under each milestone with expected outputs
        Timeline Estimates - Realistic time estimates for each phase
        Dependencies - Any task or phase that relies on another
        Tech Stack Suggestions - Recommended tools, frameworks, or platforms if applicable
        Risk Factors - Potential blockers or challenges to watch out for
        Success Metrics - How progress and completion will be measured

        Always structure the roadmap in a way that is easy to follow for both technical and non-technical stakeholders. Be specific, realistic, and prioritize clarity over complexity. If the idea is vague, make reasonable assumptions and state them clearly.""",
                ),
                (
                    "human",
                    """I have a project idea that I would like you to turn into a detailed roadmap.
        Here is my project description and idea brief:
        Project Title: {project_title}
        Project Description: {project_description}
        Target Audience: {target_audience}
        Desired Outcome: {desired_outcome}
        Available Resources (optional): {resources}
        Deadline or Timeline Preference (optional): {timeline}
        Based on the above, please generate a complete project roadmap with all phases, milestones, tasks, timelines, dependencies, and recommendations clearly laid out.""",
                ),
            ]
        )
        self.parser = langchain_core.output_parsers.PydanticOutputParser(
            pydantic_object=schemas.ProjectRoadmapInput
        )
        self.parsing_prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
                You are a precise data extraction assistant. Your job is to read a user's free-form project description and extract the relevant information into a strict JSON format.
        Extract the following fields from the user's message:

        project_title - The name or title of the project. If not explicitly stated, infer a short suitable title from the description.
        project_description - A clear and complete description of the project idea. Use the user's own words as much as possible.
        target_audience - Who the project is intended for. If not mentioned, make a reasonable inference and note it.
        desired_outcome - The goal or expected result the user wants to achieve with this project.
        resources - Any mentioned tools, team size, budget, or technology. Set to null if not mentioned.
        timeline - Any mentioned deadlines or time preferences. Set to null if not mentioned.

        Rules:

        Always return a valid JSON object and nothing else — no explanation, no markdown, no extra text.
        If a required field is missing or unclear, make a reasonable inference based on context and fill it in.
        If an optional field (resources, timeline) is not mentioned, set its value to null.
        Keep all values as plain strings.
        Do not add any fields that are not listed above.
resources - Any mentioned tools, team size, budget, or technology.

IMPORTANT:
The resources field MUST be a single string.
Do NOT return an object, dictionary, list, or nested JSON.

Correct:
"Team size: 10-15 members; Budget: 500000 USD; Tools: React Native, Node.js, MongoDB"

Incorrect:
{{
  "team_size": "...",
  "budget": "...",
  "tools": [...]
}}
        Output format:{fi}
                """,
                ),
                ("human", "{data}"),
            ]
        )
        self.parsing_prompt = self.parsing_prompt.partial(
            fi=self.parser.get_format_instructions()
        )
