JOB_ROLES = {
    "Full Stack Developer": {
        "skills": ["html", "css", "javascript", "react", "node", "sql", "git","angular"]
    },

    "Data Analyst": {
        "skills": ["python", "sql", "excel", "data analysis", "power bi"]
    },

    "ML Engineer": {
        "skills": ["python", "machine learning", "data analysis"]
    },

    "Backend Developer": {
        "skills": ["python", "java", "fastapi", "django", "sql", "docker"]
    },

    "Frontend Developer": {
        "skills": ["html", "css", "javascript", "react", "git"]
    },

    "DevOps Engineer": {
        "skills": ["docker", "kubernetes", "aws", "linux", "git"]
    },

    "Software Tester": {
        "skills": ["manual testing", "selenium", "java", "test cases", "jira"]
    }
}
from backend.job_matcher import JOB_ROLES

def match_jobs(resume_skills):
    results = {}

    resume_skills = set(resume_skills)

    for role, data in JOB_ROLES.items():
        required_skills = set(data["skills"])
        matched = resume_skills.intersection(required_skills)

        score = int((len(matched) / len(required_skills)) * 100)

        results[role] = {
            "match_percentage": score,
            "matched_skills": list(matched),
            "missing_skills": list(required_skills - matched)
        }

    return results