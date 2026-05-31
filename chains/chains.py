import utils
import langchain_core.output_parsers


def tool_chain(query, pps):
    parsing_chain = pps.parsing_prompt | utils.llm | pps.parser
    prompt_data = parsing_chain.invoke({"data": query})
    output_chain = (
        pps.prompt | utils.llm | langchain_core.output_parsers.StrOutputParser()
    )
    return output_chain.invoke(prompt_data.model_dump())
