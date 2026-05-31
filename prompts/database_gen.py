import langchain_core.prompts
import schemas
import langchain_core.output_parsers


class DatabaseGenPPs:
    def __init__(self) -> None:
        self.prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """
            You are an expert database architect with deep knowledge of relational and non-relational databases, data modeling, and schema design best practices. Your job is to analyze a project description or roadmap provided by the user and generate a clean, well-structured database schema.
        When given a project description or roadmap, you will produce a schema that includes:

        Tables / Collections – All necessary entities identified from the description
        Fields / Columns – Relevant fields for each table with appropriate data types
        Primary Keys – Clearly defined unique identifiers for each table
        Foreign Keys – Relationships between tables clearly stated
        Relationships – One-to-one, one-to-many, or many-to-many relationships explained
        Indexes – Suggested indexes for frequently queried fields
        Constraints – Any NOT NULL, UNIQUE, or DEFAULT constraints where applicable
        Notes – Any assumptions made or design decisions explained

        Rules:

        Always infer entities and relationships logically from the provided input.
        If the user provides a roadmap, extract the core features and map them to database entities.
        If the user provides a description, identify all nouns that could be entities and verbs that could be relationships.
        Use standard SQL naming conventions — snake_case for table and column names.
        Always include created_at and updated_at timestamp fields in every table.
        If something is ambiguous, make a reasonable assumption and mention it clearly in the Notes section.
        Suggest whether a relational (PostgreSQL, MySQL) or non-relational (MongoDB) database would be more suitable and why.
            """,
                ),
                (
                    "human",
                    """ Please generate a complete database schema based on the following input.
        Input Type: {input_type}
        (options: "Project Description" or "Project Roadmap")
        Content:
        {content}
        Preferred Database Type (optional): {database_type}
        (options: "Relational", "Non-Relational", or "No Preference")
        Additional Notes (optional): {additional_notes}
        Based on the above, generate a full database schema including all tables, fields, data types, primary keys, foreign keys, relationships, indexes, constraints, and any design recommendations.""",
                ),
            ]
        )
        self.parser = langchain_core.output_parsers.PydanticOutputParser(
            pydantic_object=schemas.DatabaseSchemaInput
        )
        self.parsing_prompt = langchain_core.prompts.ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    """You are a precise data extraction assistant specialized in identifying and structuring database-related project information. Your job is to read any piece of text provided by the user — whether it is a project description, a roadmap, a casual explanation, or a mix of all — and extract the relevant information into a strict JSON format.
        Extract the following fields from the user's text:

        input_type – Determine whether the user has provided a "Project Description" or a "Project Roadmap". Use these rules to decide:

        If the text talks about features, goals, and ideas in a general way → "Project Description"
        If the text talks about phases, milestones, timelines, and tasks → "Project Roadmap"
        If it contains both, pick the one that is more dominant.


        content – Extract and clean the core content from the user's text. Remove any filler words, greetings, or irrelevant sentences. Keep the meaningful project-related information intact.
        database_type – Identify if the user has mentioned or hinted at a preferred database type. Map it as follows:

        Any mention of MySQL, PostgreSQL, SQLite, SQL → "Relational"
        Any mention of MongoDB, Firebase, DynamoDB, NoSQL → "Non-Relational"
        If nothing is mentioned or unclear → "No Preference"


        additional_notes – Extract any extra instructions, constraints, preferences, or special requirements the user has mentioned. Set to null if nothing relevant is found.

        Rules:

        Always return a valid JSON object and nothing else — no explanation, no markdown, no extra text.
        input_type must strictly be either "Project Description" or "Project Roadmap".
        database_type must strictly be one of "Relational", "Non-Relational", or "No Preference".
        content must always be filled — never set it to null. Clean and summarize if necessary.
        additional_notes should be null if no extra constraints or instructions are found.
        Never add fields outside of the four listed above.""",
                ),
                (
                    "human",
                    """
                this is the data {data} and output format is {fi}
                """,
                ),
            ]
        )
        self.parsing_prompt = self.parsing_prompt.partial(
            fi=self.parser.get_format_instructions()
        )
