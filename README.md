# 🤖 AI Resume Screening Agent

An open-source AI-powered Resume Screening Agent that reads resumes (PDF/DOCX), scores them based on job relevance, and sends personalized feedback via email — all with a single click.

## 🌐 Live Demo

👉 https://resume-analyseryogi.streamlit.app/

---

## 🚀 Features

- 📂 Upload resumes in PDF or DOCX format
- 📊 Analyze and score resumes using AI (based on experience, skills, and formatting)
- 🧠 NLP-based keyword extraction and matching
- 📧 Send personalized feedback via email
- 🗃️ Logs each screening for future reference
- 🖥️ Streamlit-based Web UI

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **NLP**: spaCy, NLTK
- **File Handling**: PyPDF2, python-docx
- **Email**: smtplib, email-validator
- **ML Scoring**: Custom heuristic model (can be replaced with trained ML model)

---

## 🛠️ Installation

```bash
# Clone the repo
git clone https://gitlab.com/your-username/resume-screening-agent.git
cd resume-screening-agent

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# 🏃 Running the App

streamlit run app.py
