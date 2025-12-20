from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def generate_career_report(
    filename,
    best_role,
    placement_score,
    secondary_roles,
    growth_skills,
    future_skills
):
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)

    pdf_path = f"{reports_dir}/{filename}_career_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4

    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, y, "Career Recommendation Report")

    y -= 30
    c.setFont("Helvetica", 10)
    c.drawString(50, y, f"Generated on: {datetime.now().strftime('%d-%m-%Y')}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Best Suitable Role")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(70, y, f"{best_role}")

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Placement Score")
    y -= 20
    c.setFont("Helvetica", 12)
    c.drawString(70, y, f"{placement_score}%")

    y -= 30
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Secondary Role Suggestions")
    y -= 20
    c.setFont("Helvetica", 11)
    for role in secondary_roles:
        c.drawString(70, y, f"- {role}")
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Skills to Improve (Growth Skills)")
    y -= 20
    c.setFont("Helvetica", 11)
    for skill in growth_skills:
        c.drawString(70, y, f"- {skill}")
        y -= 15

    y -= 20
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Future-Proof Skills")
    y -= 20
    c.setFont("Helvetica", 11)
    for skill in future_skills:
        c.drawString(70, y, f"- {skill}")
        y -= 15

    c.showPage()
    c.save()

    return pdf_path
