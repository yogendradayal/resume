# main.py

import os
from resume_parser import parse_resume
from scorer import score_resume
from email_sender import send_feedback
from utils import setup_logging, mask_email
from config import RESUME_FOLDER
import logging

def process_resumes():
    setup_logging()
    for filename in os.listdir(RESUME_FOLDER):
        if filename.endswith((".pdf", ".docx")):
            path = os.path.join(RESUME_FOLDER, filename)
            parsed = parse_resume(path)
            score, breakdown = score_resume(parsed)

            masked = mask_email(parsed['email'])

            logging.info(f"Processed: {parsed['name']} ({masked}) | Score: {score}")
            print(f"Scored: {parsed['name']} - {score}")

            if parsed["email"] != "N/A":
                success = send_feedback(parsed["email"], parsed["name"], score, breakdown)
                if success:
                    logging.info(f"Email sent to: {masked}")
                else:
                    logging.error(f"Email failed for: {masked}")

if __name__ == "__main__":
    process_resumes()
