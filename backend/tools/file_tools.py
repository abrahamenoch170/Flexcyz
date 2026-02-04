from pathlib import Path

BASE_DIR = Path("workspace")
BASE_DIR.mkdir(exist_ok=True)

def list_files():
    return [str(p.relative_to(BASE_DIR)) for p in BASE_DIR.rglob("*") if p.is_file()]

def read_file(path: str):
    file_path = BASE_DIR / path
    if not file_path.exists():
        return ""
    return file_path.read_text()

def write_file(path: str, content: str):
    file_path = BASE_DIR / path
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content)
    return f"{path} written"
