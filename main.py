import json
import os
import streamlit as st

from langchain.agents import create_agent
from agent import planner_agent
from tools import *
from utils import llm

MEMORY_FILE = "memory/chat_history.json"

os.makedirs("memory", exist_ok=True)


def load_messages():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_messages(messages):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(
            messages,
            f,
            ensure_ascii=False,
            indent=2,
        )


st.set_page_config(
    page_title="BuildWise",
    page_icon="🏗️",
)

st.title("🏗️ BuildWise")
st.caption("AI Software Architect")

if "messages" not in st.session_state:
    st.session_state.messages = load_messages()

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Describe your project...")

if user_input:

    # Show user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
        }
    )

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = planner_agent.invoke({"messages": st.session_state.messages})

            assistant_message = result["messages"][-1].content

            st.markdown(assistant_message)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_message,
        }
    )

    save_messages(st.session_state.messages)

if st.sidebar.button("Clear Memory"):

    st.session_state.messages = []

    save_messages([])

    st.rerun()
