import streamlit as st
import google.generativeai as genai
from google.api_core import exceptions as google_exceptions
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

## configure gemini model with API key
api_key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.50,
    "top_p": 0.95,
    "top_k": 1,
    "max_output_tokens": 99998,
}

## system prompt for generating reply to tweet/response to comment
prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                f"""You are one of the best and popular content creators of Spillmate on Twitter.
                Spillmate is the brand for a project aimed to provide quality mental health support for everyone right on your fingertips.
                Spillmate has a mobile app with an AI powered CBT therapist chatbot that delivers personalized assistance
                based on the science of Cognitive Behavioral therapy (CBT).
                Write a reply of one or two sentences to the tweet as per the chat message you get. If it is a comment, write a relevant response maintaining the consistency and brand tone.""",
            ),
            ("human", "{chat_message}"),
        ]
    )

## page title
st.set_page_config(page_title="Generate a Reply to a Tweet/Response to a Comment")

## generate response as per input prompt
def get_response(messages, model="gemini-pro"):
    model = genai.GenerativeModel(model)
    res = model.generate_content(messages, generation_config=generation_config, prompt=prompt)
    return res

## Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
messages = st.session_state["messages"]


## Initialize session state for chat history if it doesn't exist
if messages:
    for item in messages:
        role, parts = item.values()
        if role == "user":
            st.chat_message("user").markdown(parts[0])
        elif role == "model":
            st.chat_message("assistant").markdown(parts[0])
## User input
chat_message = st.chat_input("What's your idea for your response")

res = None
if chat_message:
    st.chat_message("user").markdown(chat_message)
    res_area = st.chat_message("assistant").markdown("...")
    messages.append(
            {"role": "user", "parts":  [chat_message]},
        )
    try:
        res = get_response(messages)
    except google_exceptions.InvalidArgument as e:
        if "API key not valid" in str(e):
            st.error("API key not valid. Please pass a valid API key.")
        else:
            st.error("An error occurred. Please refresh your page and try again.")
    except Exception as e:
        logging.error(e)
        st.error("Error occured. Please refresh your page and try again.")

## To check inappropriate words in input response
if res is not None:
        res_text = ""
        for chunk in res:
            if chunk.candidates:
                res_text += chunk.text
            if res_text == "":
                res_text = "inappropriate words"
                st.error("Your words violate the rules that have been set. Please try again!")
        res_area.markdown(res_text)

