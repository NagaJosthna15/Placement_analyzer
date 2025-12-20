def recommend_growth_skills(job_matches):
    growth = set()

    for data in job_matches.values():
        if data["match_percentage"] >= 60:
            growth.update(data["missing_skills"])

    return list(growth)
