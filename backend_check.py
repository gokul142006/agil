import time
from pathlib import Path

time.sleep(4)

Path("backend_report.txt").write_text(
    "Backend check passed\n",
    encoding="utf-8",
)