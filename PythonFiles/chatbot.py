from dotenv import load_dotenv
import dbToText as db

load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDRrXrUw7vs_2iXpivVNEGQN1vxTwAP6b4")
database = db.get_str()
## function to load Gemini Pro model and get repsonses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, I am going to give you a database of expense tracker website. mostly it contains 2 tables, one is expense and another is budget. Give proper and correct output based on the inputs and numericals"},
        {"role": "model", "parts": "Great to meet you. For sure, I will be numerically correct and solve the questions"},
        {"role": "user", "parts" : database+ " Be precision with the numericals and say only 1 line of answer"}
    ])



def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))
st.subheader("The Chat History is")

for role, text in st.session_state['chat_history']:
    if(role == "Bot"):
        st.write(f"{role}: {text}")