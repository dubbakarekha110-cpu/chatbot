import streamlit as st
import ollama

#page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖"
)

#tittle
st.title("🤖 MY AI CHATBOT")
st.caption("Powered by Ollama + Streamlit")

#initialize converstion history
if "messages" not in st.session_state:
    st.session_state.messages=[]
    
#Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
#chat input
prompt=st.chat_input("Type your message... ")

if prompt:
    
    #Store user messages
    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )
    
    #Display user mesaages
    with st.chat_message("user"):
        st.write(prompt)
        
    #Get responses from Ollama
    response=ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )
    answer=response["message"]["content"]
    
    #store AI response
    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )
    
    #Display AI responses
    with st.chat_message("assistant"):
        st.write(answer)
    
    
    
    
