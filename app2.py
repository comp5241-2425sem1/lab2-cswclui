import streamlit as st
import llm


# Create a text input box
text_input = st.text_input("Enter some text:")

# Create a submit button
if st.button("Submit"):
    # Call the answer function from llm.py
    system_prompt = "Answer user question with funny tone with Emojis"
    response = llm.answer(system_prompt, text_input)
    st.write("Bot:", response)

