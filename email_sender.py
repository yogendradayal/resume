# email_sender.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_ADDRESS, EMAIL_PASSWORD, FEEDBACK_TEMPLATE_PATH
from utils import mask_email

def load_template():
    with open(FEEDBACK_TEMPLATE_PATH, 'r') as f:
        return f.read()

def send_feedback(email_to, name, score, breakdown):
    subject = "Your Resume Feedback and Score"
    body_template = load_template()
    
    breakdown_text = '\n'.join([f"{k}: {v}" for k, v in breakdown.items()])
    body = body_template.format(name=name, score=score, breakdown=breakdown_text)

    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email_to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, email_to, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
