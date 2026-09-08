# AI-Powered CV Critiquer
 
A lightweight Streamlit app that uses a locally-running LLM (via [Ollama](https://ollama.com)) to analyze a resume/CV and provide structured, constructive feedback — optionally tailored to a specific job role.
 
## Features
 
- Upload a CV as **PDF or TXT**
- Optionally specify a **target job role** for tailored feedback
- Get AI-generated feedback on:
  - Content clarity and impact
  - Skills presentation
  - Experience descriptions
  - Role-specific improvement suggestions
- Runs entirely **locally** — no data leaves your machine, since the LLM runs through Ollama rather than a cloud API

## Demo
 
Example output for a CV targeted at an "AI Intern" role:
 
- **Overall Impression** — a short summary of the candidate's background and general fit
- **Content Clarity and Impact** — flags issues like vague objective statements, missing quantifiable achievements, and inconsistent formatting
- **Skills Presentation** — suggestions like using bullet points, prioritizing relevant skills, and quantifying proficiency
- **Experience Descriptions** — recommends action verbs, specificity, and impact-focused phrasing
- **Specific Improvements** for the target role — e.g., highlighting AI/ML skills and relevant projects for an AI Intern position
- **Additional Recommendations** and a numbered **Action Plan** to guide revisions
## Tech Stack
 
| Component | Purpose |
|---|---|
| [Streamlit](https://streamlit.io) | Web app UI |
| [Ollama](https://ollama.com) | Runs the LLM locally |
| `llama3.2` | Default model used for analysis |
| PyPDF2 | Extracts text from uploaded PDF files |
| python-dotenv | Loads environment variables (e.g., configurable model name) |
 
## How It Works
 
1. The user uploads a CV (PDF or TXT) and optionally enters a target job role.
2. On clicking **Analyze my CV**, the app extracts raw text from the file:
   - PDFs are parsed page-by-page using `PyPDF2`
   - TXT files are read and decoded directly
3. The extracted text is inserted into a structured prompt asking the model to critique the CV across four dimensions (clarity, skills, experience, role-fit).
4. The prompt is sent to a local LLM via `ollama.chat()`, using a system prompt that frames the model as an experienced HR/recruitment reviewer.
5. The model's response is rendered back in the app as formatted markdown.
## Prerequisites
 
- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running locally
- A pulled model (default: `llama3.2`):
```bash
  ollama pull llama3.2
```
 
## Installation
 
```bash
git clone <your-repo-url>
cd ai-cv-critiquer
pip install -r requirements.txt
```
 
**requirements.txt**
```
streamlit
PyPDF2
python-dotenv
ollama
```
 
## Usage
 
1. Start Ollama (if not already running):
```bash
   ollama serve
```
2. Run the app:
```bash
   streamlit run app.py
```
3. Open the local URL Streamlit provides (usually `http://localhost:8501`)
4. Upload a CV, optionally enter a target job role, and click **Analyze my CV**

## Notes & Limitations
 
- Response time depends on your hardware (CPU vs. GPU inference) and the size of the model — larger models like `llama3.3:70b` give richer feedback but take longer to run.
- Scanned/image-based PDFs (no embedded text layer) will not extract properly with `PyPDF2`; only text-based PDFs are supported.
- Since inference runs locally, no CV data is sent to any external API — feedback quality depends entirely on the chosen local model.

## Possible Future Improvements
 
- Stream responses token-by-token for better perceived performance
- Return structured (JSON) output with a numeric score and categorized feedback for a cleaner UI
- Support additional file formats (`.docx`)
- Add a model selector so users can choose between speed and quality
- Downloadable feedback report (PDF/TXT)
