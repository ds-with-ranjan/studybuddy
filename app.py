import streamlit as st
import os
import json

def load_questions():
    # Get the absolute path of this script
    base_dir = os.path.dirname(__file__)
    # Build full path to questions.json inside data folder
    file_path = os.path.join(base_dir, "data", "questions.json")
    
    # Open and load the JSON file
    with open(file_path, "r") as file:
        questions = json.load(file)
    return questions

def main():
    st.title("Study Buddy - Questions Viewer")

    # Load questions data
    try:
        questions_data = load_questions()
    except FileNotFoundError:
        st.error("Error: 'questions.json' file not found in the 'data' folder.")
        return
    except json.JSONDecodeError:
        st.error("Error: 'questions.json' contains invalid JSON.")
        return
    
    # Show the questions
    st.header("Questions:")
    for idx, q in enumerate(questions_data, start=1):
        st.write(f"**Q{idx}:** {q['question']}")
        if 'options' in q:
            for opt in q['options']:
                st.write(f"- {opt}")
        st.write("---")

if __name__ == "__main__":
    main()
