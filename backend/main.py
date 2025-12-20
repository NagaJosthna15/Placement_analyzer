from fastapi import FastAPI, UploadFile, File, HTTPException
from backend.resume_parser import extract_text_from_pdf
from backend.skill_extractor import extract_skills, calculate_final_result
from backend.job_matcher import match_jobs
from backend.recommender.secondary_role import recommend_secondary_role
from backend.recommender.growth_skills import recommend_growth_skills
from backend.recommender.future_skills import recommend_future_skills
from backend.reports.pdf_report import generate_career_report
from backend.utils.score_utils import get_score_color, is_ready_for_placement
from backend.utils.save_report import save_as_json, save_as_pdf



app = FastAPI(
    title="Placement Analyzer API",
    description="AI-powered Resume Analyzer & Career Recommendation System",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"status": "success", "message": "API is running successfully"}

@app.post("/upload-resume/",tags=["Resume Analysis"])
async def upload_resume(file: UploadFile = File(...)):

    # ✅ File validation
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    try:
        text = extract_text_from_pdf(file.file)
    except Exception:
        raise HTTPException(status_code=500, detail="Unable to read PDF")

    if not text.strip():
        raise HTTPException(status_code=400, detail="Resume is empty")

    skills = extract_skills(text)
    if not skills:
        raise HTTPException(status_code=400, detail="No skills found in resume")

    job_matches = match_jobs(skills)
    best_role, placement_score = calculate_final_result(job_matches)

    # ✅ Call once only
    secondary_roles = recommend_secondary_role(job_matches, best_role)
    growth_skills = recommend_growth_skills(job_matches)
    future_skills = recommend_future_skills(skills)

    score_color = get_score_color(placement_score)
    ready_status = is_ready_for_placement(placement_score)


    pdf_path = generate_career_report(
    filename=file.filename.replace(".pdf", ""),
    best_role=best_role,
    placement_score=placement_score,
    secondary_roles=secondary_roles,
    growth_skills=growth_skills,
    future_skills=future_skills
)


    return {
        "status": "success",
        "data": {
            "filename": file.filename,
            "skills_found": skills,
            "total_skills": len(skills),
            "job_match": job_matches,
            "best_role": best_role,
            "placement_score": placement_score,
            "secondary_roles": secondary_roles,
            "growth_skills": growth_skills,
            "future_skills": future_skills,
             "ready_for_placement": ready_status,
            "score_color": score_color,
            "carrer_report_pdf":pdf_path
        }
    }
