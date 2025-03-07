import streamlit as st
import NeuraForge as n


def Text(Text):
    st.text(Text)
def Title(Title):
    st.title(Title)

def Input(input):
    st.text_input(input)

def API(api):
    n.Api(api)

def chatt(chat):
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Say something..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)


        # Generate bot response (simple echo bot for now)
        response = n.Send(chat, prompt)
        
        # Display bot response
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)



