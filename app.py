import streamlit as st
from resume_parser import parse_resume
from scorer import score_resume
from email_sender import send_feedback as send_feedback_email
from config import EMAIL_ADDRESS

st.set_page_config(page_title="Resume Scoring Agent", layout="centered")
st.title("📄 AI Resume Scoring & Feedback Agent")

uploaded_file = st.file_uploader("Upload a Resume (.pdf or .docx)", type=["pdf", "docx"])

if uploaded_file:
    # Save the uploaded resume
    file_path = f"resumes/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    # Parse the resume
    st.info("🔍 Parsing Resume...")
    parsed_data = parse_resume(file_path)
    st.success("✅ Resume Parsed!")

    # Show parsed data
    st.subheader("🧠 Extracted Resume Info:")
    for key, value in parsed_data.items():
        st.write(f"**{key.capitalize()}**: {value}")

    # Score the resume
    st.subheader("📊 Resume Score:")
    score, feedback = score_resume(parsed_data)
    st.metric("Total Score", f"{score}/100")
    st.text_area("📋 Feedback", feedback, height=200)

    # Optionally send email
    if st.button("✉️ Send Feedback Email"):
        email = parsed_data.get("email")
        name = parsed_data.get("name", "Candidate")
        if email:
            try:
                send_feedback_email(email, name, score, feedback)
                st.success(f"Email sent to {email}")
            except Exception as e:
                st.error(f"Failed to send email: {str(e)}")
        else:
            st.warning("No email found in resume.")
