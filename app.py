from resume_parser import extract_skills
from agent_logic import agent_decision

resume_text = input("Paste resume text: ")
job_role = input("Enter job role (AI / Data / Software): ")

job_skill_map = {
    "ai": ["python", "machine learning", "ai", "nlp"],
    "data": ["python", "sql", "data analysis"],
    "software": ["java", "python", "sql"]
}

resume_skills = extract_skills(resume_text)
result = agent_decision(resume_skills, job_skill_map.get(job_role.lower(), []))

print("\nAgent Decision Report")
print("Score:", result["score"])
print("Matched Skills:", result["matched_skills"])
print("Recommendation:", result["recommendation"])
