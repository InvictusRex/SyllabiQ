import streamlit as st
import os
from backend import parser, matcher, analyzer
from models.sentence_model import load_model
from utils.file_utils import save_uploaded_file

UPLOAD_DIR = "assets/example_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

st.set_page_config(page_title="SyllabiQ", layout="wide")
st.title("📘 SyllabiQ – Prioritize Your Exam Topics Using PYQs")

# Upload syllabus
syllabus_file = st.file_uploader("Upload Syllabus PDF", type=["pdf"])
pyq_file = st.file_uploader("Upload PYQs PDF", type=["pdf"])

if syllabus_file and pyq_file:
    st.success("Files uploaded successfully!")

    # Save and extract
    syllabus_path = save_uploaded_file(syllabus_file, os.path.join(UPLOAD_DIR, syllabus_file.name))
    pyq_path = save_uploaded_file(pyq_file, os.path.join(UPLOAD_DIR, pyq_file.name))

    syllabus_text = parser.extract_text_from_pdf(syllabus_path)
    pyq_text = parser.extract_text_from_pdf(pyq_path)

    # Naive splitting of topics and questions
    topics = [line.strip() for line in syllabus_text.split("\n") if len(line.strip()) > 5]
    questions = [q.strip() for q in pyq_text.split("\n") if len(q.strip()) > 10]

    st.write(f"📝 Detected **{len(topics)}** topics and **{len(questions)}** questions.")

    # Load model
    with st.spinner("Matching questions to topics..."):
        model = load_model()
        topic_question_map = matcher.match_questions_to_topics(questions, topics, model)
        categorized = analyzer.categorize_topics(topic_question_map)

    st.header("📊 Topic Categorization")
    for category, topic_list in categorized.items():
        st.subheader(f"🔷 {category}")
        for topic, freq in topic_list:
            st.markdown(f"**{topic}** – {freq} question(s)")
            for q in topic_question_map[topic]:
                st.markdown(f"- {q}")
