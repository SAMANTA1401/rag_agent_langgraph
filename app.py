import streamlit as st
from transformers import pipeline
from chatbot import chatbot

mybot=chatbot()
workflow=mybot() # call class as function with special __call__ method


# Set up the Streamlit app UI
st.title("ChatBot with LangGraph")
st.write("Ask any question, and I'll try to answer it!")

# Input text box for the question
question = st.text_input("Enter your question here:")
input={"messages": [question]}

# Button to get the answer
if st.button("Get Answer"):
    if input:
        response=workflow.invoke(input)
        st.write("**Answer:**", response['messages'][-1].content)
    else:
        st.warning("Please enter a question to get an answer.")

# Additional styling (optional)
st.markdown("---")
st.caption("Powered by Streamlit and Transformers")