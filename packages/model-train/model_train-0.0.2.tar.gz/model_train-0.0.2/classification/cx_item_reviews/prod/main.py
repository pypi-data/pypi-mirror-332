from pathlib import Path
import subprocess


path = Path.home() / "PycharmProjects/model_train/classification/cx_item_reviews/prod"
lst = [
    path / "download_data.py",
    path / "inference.py"
]
for f in lst:
    result = subprocess.run(["python", str(f)], capture_output=True, text=True)
