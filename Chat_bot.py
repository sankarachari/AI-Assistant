from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(), override=True)

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

import streamlit as st
from streamlit_chat import message

st.set_page_config(page_title="Your customised assistant", page_icon="🤖")
st.image('cloudface.jpg')
st.subheader("You can ask help on any subject")
chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    system_message = st.text_input(label='System Role')
    user_prompt = st.text_input(label='Send a message')
    if system_message:
        if not any(isinstance(msg, SystemMessage) for msg in st.session_state.messages):
            st.session_state.messages.append(
                SystemMessage(content=system_message)
            )

    if user_prompt:
        st.session_state.messages.append(
            HumanMessage(content=user_prompt)
        )    

    with st.spinner("Waiting for response..."):
        response = chat.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

st.session_state.messages  

