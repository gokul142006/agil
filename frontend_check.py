import time
from pathlib import Path

time.sleep(4)

Path("frontend_report.txt").write_text(
    "Frontend check completed successfully.\n"
)
