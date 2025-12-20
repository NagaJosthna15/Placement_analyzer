FUTURE_SKILLS = [
    "system design",
    "cloud computing",
    "microservices",
    "kubernetes",
    "ai integration",
    "data engineering"
]

def recommend_future_skills(resume_skills):
    return [
        skill for skill in FUTURE_SKILLS
        if skill not in resume_skills
    ]
