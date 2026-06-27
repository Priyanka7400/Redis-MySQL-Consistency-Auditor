from datetime import datetime
import json

report = {
    "total_records_checked": 100,
    "mismatches_found": 2,
    "consistency_score": "98.0%",
    "audit_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

print(json.dumps(report, indent=4))

with open("audit_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nAudit Report Saved Successfully!")