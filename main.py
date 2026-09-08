import streamlit as st
import PyPDF2
import io
import os
from dotenv import load_dotenv
import ollama

load_dotenv()

st.set_page_config(page_title="AI-powered CV Critiquer", layout="centered")

st.title("AI-Powered CV Critiquer")
st.markdown("Upload your CV and get AI-powered feedback!")

file = st.file_uploader("Upload your CV (pdf/txt)", type = ["pdf","txt"])
job_role = st.text_input("Enter the job role you're targeting(optional)")

analyze = st.button("Analyze my CV")

def extract_content_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_content_file(file):
    if file.type == "application/pdf":
        return extract_content_pdf(io.BytesIO(file.read()))
    return file.read().decode("utf-8")

if analyze and file:
    try:
        file_content = extract_content_file(file)

        if not file_content.strip():
            st.error("File does not have any content.")
            st.stop()

        prompt = f"""You are reviewing a resume for a candidate applying to {job_role if job_role else 'a general job application'}.
                Analyze ONLY the content provided below — do not assume or invent details that aren't present.

                Evaluate the resume across these five areas:
                1. **First Impression & Structure**
                - Is the layout clean, scannable, and professional?
                - Are section headings clear and conventional?
                2. **Content Clarity & Impact**
                - Are bullet points results-oriented rather than just listing duties?
                - Are achievements quantified (numbers, percentages, timeframes) where possible?
                3. **Skills Presentation**
                - Are skills relevant, well-organized, and free of redundancy?
                - Are the most in-demand/relevant skills for the target role easy to find?
                4. **Experience Descriptions**
                - Do bullet points start with strong action verbs?
                - Is there a clear sense of scope, ownership, and outcome for each role/project?
                5. **Role Fit — {job_role if job_role else 'General Applications'}**
                - What's missing or under-emphasized for this specific type of role?
                - What should be added, cut, or reworded to better match it?

                For your response, follow this exact format:
                ## Overall Score: X/10
                One or two sentences summarizing the resume's overall strength.

                ## Top 3 Strengths
                - ...

                ## Top 3 Areas to Improve
                - ...

                ## Detailed Feedback
                (Organized under the five headings above — 2-4 bullet points each, specific and actionable. Reference actual content from the resume where relevant, not generic advice.)

                ## Suggested Rewrites
                Pick 2-3 of the weakest bullet points from the resume and show a "before → after" rewrite.

                Resume content:
                \"\"\"
                {file_content}
                \"\"\"
                """

        response = ollama.chat(model = "llama3.2",
        messages = [
            {
                "role":"system",
                "content":"""You are an expert CV/resume reviewer 
                with years of experience in HR and recruitment"""},
            {
                "role":"user",
                "content": prompt}
        ])

        st.markdown("### Analysis Results")
        st.markdown(response['message']['content'])

    except Exception as e:
        st.error(f"An error occured: {str(e)}")