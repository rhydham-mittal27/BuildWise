import langchain_mistralai
import os
import dotenv

dotenv.load_dotenv()
llm = langchain_mistralai.ChatMistralAI(model_name=str(os.getenv("MISTRAL_MODEL")))
