import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

#Load environmental variables
load_dotenv()

#Get API key
api_key=os.getenv("GEMINI_API_KEY")

#Create Gemini clinet
clinet=genai.client(api_key=api_key)

#Page Configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    page_icon="🤖",
    layout="centered"    
)

#Title
st.title("🤖 Gemini AI Chatbot")

st.write("Ask Gemini Anything!")

#User prompt
prompt=st.text_area(
    "Enter your prompt:",
    placeholder="Explain Aritifical Intelligent in simple words..."
)
#Generate button
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Gemini is thinking..."):
            response=clinet.models.generate_content(
                model="gemini-3.5-flash-lite",
                content=prompt
            )
            st.success("Response genereted!")
            st.write(response.text)
    else:
        st.warning("Please enter a prompt.")
