# resume_parser.py

import os
import re
from docx import Document
from PyPDF2 import PdfReader

def extract_text_from_docx(path):
    doc = Document(path)
    return '\n'.join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(path):
    text = ''
    with open(path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    text = extract_text_from_docx(file_path) if ext == '.docx' else extract_text_from_pdf(file_path)

    name_match = re.search(r"(?:Name|Full Name)\s*:\s*(.+)", text, re.IGNORECASE)
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    grad_year = re.search(r"(20\d{2})", text)

    return {
        "name": name_match.group(1) if name_match else "N/A",
        "email": email_match.group(0) if email_match else "N/A",
        "grad_year": grad_year.group(0) if grad_year else "N/A",
        "text": text
    }
