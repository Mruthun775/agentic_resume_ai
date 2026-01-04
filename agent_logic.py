def agent_decision(resume_skills, job_skills):
    score = 0
    matched = []

    for skill in job_skills:
        if skill.lower() in resume_skills:
            score += 10
            matched.append(skill)

    recommendation = "Strong Fit" if score >= 30 else "Moderate Fit" if score >= 10 else "Not Suitable"

    return {
        "score": score,
        "matched_skills": matched,
        "recommendation": recommendation
    }
