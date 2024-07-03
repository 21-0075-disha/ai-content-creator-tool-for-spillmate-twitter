# Spillmate's Twitter Content Creator Automation Tool 🪴
**Objective:** To automate content creation for Spillmate's Twitter (X) account, ensuring consistency in brand tone and optimizing content for better engagement.

**This app uses login authentication. Only registered users can benefit from this tool.**

### How it works:
The content creator is presented with the options to:
- create a tweet with relevant content and hashtags to promote Spillmate, or
- generate a response (reply) to a given tweet.

Choosing any of these options will take you to a page where you can type your idea about the tweet or reply (the user prompt).
You will instantly get a customized tweet or reply with relevant content and consistent tone with regard to Spillmate.

This tool is powered by Google Gemini AI and Langchain is used for developing this LLM application.

### Steps to Set Up this App
- Clone the repo with ```git clone https://github.com/21-0075-disha/ai-content-creator-tool-for-spillmate-twitter.git```
- Install and configure a Python Virtual Environment (Anaconda or Miniconda)
- Install all required dependencies (libraries) with ```pip install -r requirements.txt```
- In the parent directory ```ai-content-creator-tool-for-spillmate-twitter```, create a ```.env``` file with ```GOOGLE_API_KEY=<Your API Key here>```
- To run the Streamlit app, use ```streamlit run app-home-page.py```

---
Currently I am using a script to generate hashed passwords for users and store them in a pickle file (for authorization part).
This can be improved by opting for a file ```.streamlit/secrets.toml``` which will store the user's email and password (will be doing that later).
I will also be using Ideogram AI to generate relevant images for better engagement with the content.
