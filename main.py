import streamlit as st
from backend.utils import extract_text_from_pdf
from classifier import ask_gpt

st.set_page_config(page_title="Topic Frequency Analyzer", layout="wide")

st.title("📘 Exam Topic Frequency Analyzer")
syllabus_pdf = st.file_uploader("📄 Upload Syllabus PDF", type="pdf")
pyq_pdf = st.file_uploader("📄 Upload PYQ PDF", type="pdf")

if syllabus_pdf and pyq_pdf:
    with st.spinner("🔍 Extracting syllabus..."):
        syllabus_text = extract_text_from_pdf(syllabus_pdf)

    with st.spinner("🔍 Extracting PYQ content..."):
        pyq_text = extract_text_from_pdf(pyq_pdf)

    # Reduce token load
    syllabus_lines = syllabus_text.split("\n")
    pyq_lines = pyq_text.split("\n")
    limited_syllabus = "\n".join(syllabus_lines[:20])
    limited_pyqs = "\n".join(pyq_lines[:30])

    prompt = [
        {"role": "user", "content": f"""
Given the syllabus: 
{limited_syllabus}

And the following past year questions: 
{limited_pyqs}

Classify each question under the relevant syllabus topic. Then list topics by frequency of appearance like this:

Most frequently asked:
1. Topic name
- Question 1
- Question 2
...

Moderate frequency:
...

Least Frequently asked:
...
"""}
    ]

    with st.spinner("🤖 Analyzing with Gemini..."):
        output = ask_gpt(prompt)

    st.success("✅ Classification Complete!")
    st.markdown(output, unsafe_allow_html=True)