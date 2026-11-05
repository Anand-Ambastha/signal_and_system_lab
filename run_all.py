"""Run every Python experiment and regenerate outputs/python/."""
import subprocess, sys
from pathlib import Path

py = Path(__file__).resolve().parent / "python"
for script in sorted(py.glob("exp*.py")):
    print(f"\n=== {script.name} ===")
    subprocess.run([sys.executable, script.name], cwd=py, check=True)
