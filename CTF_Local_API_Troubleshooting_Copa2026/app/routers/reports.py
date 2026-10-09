from fastapi import APIRouter

router = APIRouter(prefix="/api/reports", tags=["reports"])

REPORTS = {
    1: {"id": 1, "score": 91, "status": "ok"},
    2: {"id": 2, "score": 82, "status": "ok"},
    13: None,
}

@router.get("/{report_id}")
def get_report(report_id: int):
    report = REPORTS.get(report_id)

    if report_id not in REPORTS:
        return {"error": "report not found"}

    return {
        "id": report["id"],
        "score": report["score"],
        "status": report["status"],
    }
