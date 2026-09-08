import streamlit as st
import PyPDF2
import io
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI-powered CV Critiquer")