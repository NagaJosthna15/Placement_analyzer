import json
from datetime import datetime
import os

REPORTS_DIR = "backend/reports/saved"

os.makedirs(REPORTS_DIR, exist_ok=True)


def save_as_json(filename: str, data: dict):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"{REPORTS_DIR}/{filename}_{timestamp}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    return file_path


def save_as_pdf():
    # 🔴 Placeholder for future
    # Actual PDF generation already handled by generate_career_report
    pass
