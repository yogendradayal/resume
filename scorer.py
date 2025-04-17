# scorer.py

def score_resume(parsed_data):
    text = parsed_data["text"].lower()

    keywords = ["machine learning", "deep learning", "pandas", "sklearn", "python", "ai", "llm", "transformer", "llama", "streamlit"]
    score = sum(1 for kw in keywords if kw in text)

    score_breakdown = {
        "AI Keywords Matched": score,
        "Education Found": 10 if "b.tech" in text or "bachelor" in text else 0,
        "Experience Found": 10 if "experience" in text or "internship" in text else 0,
        "Formatting": 5 if len(text) > 500 else 2,
    }

    total_score = sum(score_breakdown.values())
    return total_score, score_breakdown
