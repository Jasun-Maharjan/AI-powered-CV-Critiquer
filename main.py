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

        prompt = f""""""
