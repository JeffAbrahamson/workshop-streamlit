import os

import streamlit as st
from openai import OpenAI

st.title("Chat with GPT-3.5 Turbo")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "Be concise, and reply like a poet.",
        }
    ]

# Display chat messages from history on app rerun, excluding system messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])


def get_response(messages):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(st.session_state.messages)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )
