import streamlit as st
import llm,json

# Sidebar with input box and selection box
with st.sidebar:
    topic = st.text_input("Enter the topic:")
    num_questions = st.selectbox("Select number of questions:", [1, 2, 3, 4, 5])
    
    # Create a generate button
    button  = st.button("Generate Questions")

# Display the inputs
#st.write(f"Topic: {topic}")
#st.write(f"Number of Questions: {num_questions}")

# read the prompt stored in 'prompts.txt'

with open('prompt.txt', 'r') as f:
    user_prompt = f.read()

formatted_prompt = user_prompt.replace("{topic}", topic).replace("{num_questions}", str(num_questions))

# write the prompt to the screen
st.write(formatted_prompt )

result = llm.answer("", formatted_prompt)
st.json(result)

# Parse the JSON result and print out the questions and answers
result_dict = json.loads(result)
for qa in result_dict.get("questions", []):
    st.write(f"Question: {qa['question_text']}")
    with st.expander("Show Answer"):
        st.info(f"Answer: {qa['answer']}")


