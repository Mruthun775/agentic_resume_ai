def extract_skills(resume_text):
    skills_db = [
        "python", "java", "sql", "machine learning",
        "ai", "data analysis", "nlp", "deep learning"
    ]
    resume_text = resume_text.lower()
    found_skills = [skill for skill in skills_db if skill in resume_text]
    return found_skills
