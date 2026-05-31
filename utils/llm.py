from langchain_mistralai import ChatMistralAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatMistralAI(model_name=str(os.getenv("MISTRAL_MODEL")))
