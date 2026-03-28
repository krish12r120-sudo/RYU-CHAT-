import streamlit as st
from groq import Groq

st.set_page_config(page_title="RYU CHAT")

client = Groq(api_key=st.secrets["GROQ_KEY"])

st.title("🤖 RYU CHAT")

user_input = st.chat_input("Message Ryu...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        chat = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are RYU, a friendly AI."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write(chat.choices[0].message.content)
