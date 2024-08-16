import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import requests


def app():


    genai.configure(api_key='APIKEY')
    # Initialize the Generative AI model
    model = genai.GenerativeModel("gemini-1.5-flash")


    # Streamlit app
    st.title("Generative AI for Technical Interview Preparation")
    query = st.text_input("Enter your prompt:")

    def explanation():
        context = """You are a technical assistant designed to provide short and accurate answers to technical questions for interview preparation. 
        Your goal is to deliver concise, clear, and precise responses that directly address the user's query without unnecessary detail. 
        Focus on accuracy and brevity, ensuring the information is directly relevant to the question asked. The answers should be in elaborately in point.
        Help the user with the syntax to understand more effectively And Generate a example  code for  the topic.
        """

        prompt = {query}

        chat = model.start_chat(
            history=[
                {"role": "user", "parts": context},
                {"role": "model", "parts": prompt},
            ]
        )
        response = chat.send_message(prompt)
        return response.text

    def mcq():
        context1 = """Generate 10 MCQ questions for the user with answers and explanations. Don't repeat the same question.
                    Question:
                    Answer:"""
        prompt1 = {query}
        chat = model.start_chat(
            history=[
                {"role": "user", "parts": context1},
                {"role": "model", "parts": prompt1},
            ]
        )
        response2 = chat.send_message(prompt1)
        return response2.text




    response = explanation()
    st.write(response)

    response2 = mcq()
    st.write(response2)


