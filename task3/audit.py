import json
from datetime import datetime


AUDIT_FILE = "audit_log.jsonl"


def log_step(source, status, output):

    record = {
        "timestamp": datetime.now().isoformat(),
        "source": source,
        "status": status,
        "output": output,
    }

    with open(AUDIT_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")

    print(f"[AUDIT] {source} -> {status}")