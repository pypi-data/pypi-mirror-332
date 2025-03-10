import sys
from pathlib import Path

UTF8 = {"encoding": "utf-8"}

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def maybe_backup_file(filepath: Path) -> bool:
    if not filepath.exists():
        return False
    print(f"Backuping {filepath}")
    with (
        filepath.with_suffix(".bak").open("wb") as backup,
        filepath.open("rb") as file
    ):
        backup.write(file.read())
    return True