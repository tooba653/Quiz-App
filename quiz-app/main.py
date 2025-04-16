import streamlit as st
import random 
import time

st.title("📝 Quiz Application")
questions = [
    {
        "question": "What is the National flower of Pakistan?",
        "options": ["Rose", "Lili", "Jasmine", "Sunflower"],
        "answer": "Jasmine",
    },
    {
        "question": "Does the sun rise in the east or west?",
        "options": [
            "west",
            "south",
            "East",
            "North",
              ],
        "answer": "East",
    },
    {
        "question": "What is  the largest ocean in the world?",
        "options": ["Atlantic ocean", "Indian ocean", "Arctic ocean", "Pacific ocean"],
        "answer": "Pacific ocean",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Who is known as the father of computer?",
        "options": ["Isaac Newton", "Alan Turing", "Bill Gates", "Charles Babbage"],
        "answer": "Charles Babbage",
    },
]
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question
st.subheader(question["question"])
selected_option = st.radio("Choose your answer", question["options"], key="answer")
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])
    time.sleep(5)

    st.session_state.current_question = random.choice(questions)
    
    st.rerun()