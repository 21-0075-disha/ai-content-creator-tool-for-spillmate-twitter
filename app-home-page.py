## Home page (Entrypoint)
import streamlit as st
import streamlit_authenticator as stauth
import pickle
from pathlib import Path

hide_bar= """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        visibility:hidden;
        width: 0px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        visibility:hidden;
    }
    </style>
"""

# sample usernames for auth login
names = ["Alicia Sierra", "Monica Gaztambide","Bonnie Palermo"]
usernames = ["a-sierra", "monica","bonnie_palermo"]

# load hashed passwords, hash is encryption
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "SIPL_dashboard", "abcdef")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Incorrect credentials")
    st.markdown(hide_bar, unsafe_allow_html=True)

if authentication_status == None:
    st.warning("Please enter your credentials")
    st.markdown(hide_bar, unsafe_allow_html=True)


if authentication_status:
    ## main sidebar
    st.sidebar.title(f"Welcome {name}")
    st.sidebar.success("What do you want to create?")
    st.set_page_config(
        page_title="AI Tool for Content Creation for Spillmate",
        page_icon="🪴",
    )
    st.write("To automate content creation for Spillmate's Twitter account and optimize content for better engagement")
    st.markdown("""
    - You can choose to create a Twitter post to promote Spillmate
    - You can post a comment relevant to a given post
    - You can generate responses to comments
    """)

    ## Streamlit Style of Hiding sidebar
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    # log out of the app
    authenticator.logout("Logout", "sidebar")