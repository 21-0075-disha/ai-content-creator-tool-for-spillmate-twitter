import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

## Configure Google Gemini with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Set up Google GenAI model
model = genai.GenerativeModel('gemini-pro')

system_prompt = """
    You are one of the best and popular content creators of Spillmate on Twitter.
    Spillmate is a project aimed to provide quality mental health support for everyone right on your fingertips.
    Spillmate is your pocket therapist, an AI assistant who is empathetic,
    supportive and judgement-free, and backed by science. It uses Cognitive Behavioral Therapy (CBT) principles
    and provides effective advice based on tried and tested CBT methods.
    The key content guidelines for Twitter content creation:
    1. Stick to the maximum linit of 280 characters per tweet and reply.
    2. Align with the empathetic brand image of Spillmate.
    3. The main focus is on insights, coping mechanisms and adaptive measures to take care of your mental health.
    4. Company updates, brand insights and relevant content which endorse Spillmate.
    5. Use three to five appropriate hashtags related to the brand, mental health awareness and wellbeing.
    6. Avoid using line breaks. Use suitable emojis.
    7. Avoid potentially triggering, explicit or offensive language
    8. Provide testimonials and success stories to build trust and credibility.
    9. Engagement through thoughtful questions and supportive calls-to-action.
    10. Write only the post or reply. Do not explain with headings.
"""

MAX_LENGTH = 280
def generate_required_content(prompt):
    response = model.generate_content(system_prompt + prompt)
    return response.text[:MAX_LENGTH]

## User authentication function
def authenticate(username, password):
    # Validate credentials using Streamlit secrets
    return username == st.secrets["secrets"]["USERNAME"] and password == st.secrets["secrets"]["PASSWORD"]

## Streamlit App UI
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

## Auth Wall for Login
if not st.session_state.authenticated:
    st.header("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login and Proceed to App"):
        if authenticate(username, password):
            st.session_state.authenticated = True
            st.success("Welcome Content Creator! Click again to go.")
        else:
            st.error("Invalid credentials")
else:
    ## Dropdown selector presents these options
    feature = st.selectbox("What's your idea?", ["Create a post...", "Write a reply..."])

    ## Input field (text area)
    user_input = st.text_area("Type your content creation idea")

    if st.button("Generate Content"):
        if feature == "Create a post...":
            final_response = generate_required_content(f"Write a Twitter post about {user_input}")
        elif feature == "Write a reply...":
            final_response = generate_required_content(f"Write an appropriate reply to this Twitter post: {user_input}")
        
        st.write(final_response)
