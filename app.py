import streamlit as st # type: ignore
st.title("Welcome to my ai app")

import google.generativeai as genai
genai.configure(api_key="AIzaSyCDG2E0rT4Wp1YnaBEHH8W5wathqskci5c")
text = st.text_input("Enter a prompt")
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("click me"):
    response = chat.send_message(text)
    st.write(response.text)