import streamlit as st

st.set_page_config(page_title="My AI ChatBot", page_icon="🤖")

st.title("🤖 My AI ChatBot")
st.write("Welcome to my chatbot!")
prompt = st.text_input("", placeholder="Ask something...")

if st.button("Generate"):
    if prompt:
        st.write(f"**You:** {prompt}")
        st.write(f"**Bot:** You asked: {prompt}")
    else:
        st.warning("Please enter a question.")
        
        