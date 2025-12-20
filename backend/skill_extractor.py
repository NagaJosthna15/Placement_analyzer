import re

SKILLS_DB = [
    "python", "java", "c", "c++", "sql",
    "html", "css", "javascript","data analysis",
    "react", "node", "fastapi", "django",
    "machine learning", "data analysis",
    "power bi", "excel", "git", "docker", "aws"
]

def extract_skills(text: str):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.append(skill)

    return list(set(found_skills))

def calculate_final_result(job_matches):
    total = 0
    best_role = ""
    best_score = 0

    for role, data in job_matches.items():
        score = data["match_percentage"]
        total += score

        if score > best_score:
            best_score = score
            best_role = role

    placement_score = total // len(job_matches)

    return best_role, placement_score

