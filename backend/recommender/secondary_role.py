def recommend_secondary_role(job_matches, best_role):
    return [
        role for role, data in job_matches.items()
        if role != best_role and data["match_percentage"] >= 50
    ]
