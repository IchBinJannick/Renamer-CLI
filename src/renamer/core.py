import os
import re
from datetime import datetime
from pathlib import Path

def getFiles(folder: Path, pattern: str | None) -> list[Path]:
    files = [f for f in folder.iterdir() if f.is_file()]
    if pattern:
        files = [f for f in files if re.search(pattern, f.name)]
    return sorted(files)

def renameReplace(files: list[Path], old: str, new: str, dry_run: bool) -> list[tuple[str, str]]:
    results = []
    for f in files:
        newName = f.name.replace(old, new)
        results.append((f.name, newName))
        if not dry_run and newName != f.name:
            f.rename(f.parent / newName)
    return results

def renameNumber(files: list[Path], prefix: str, dry_run: bool) -> list[tuple[str, str]]:
    results = []
    for i, f in enumerate(files, start=1):
        newName = f"{prefix}{i:03d}{f.suffix}"
        results.append((f.name, newName))
        if not dry_run:
            f.rename(f.parent / newName)
    return results

def renameByDate(files: list[Path], use_created: bool, dry_run: bool) -> list[tuple[str,str]]:
    results = []
    for f in files:
        ts = f.stat().st_birthtime() if use_created else f.stat().st_mtime
        date_str = datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        newName = f"{date_str}_{f.name}"
        results.append((f.name, newName))
        if not dry_run:
            f.rename(f.parent / newName)
    return results

def renameExtension(files: list[Path], oldExt: str, newExt: str, dry_run: bool) -> list[tuple[str, str]]:
    results = []
    for f in files:
        if f.suffix.lower() == oldExt.lower():
            newName = f.stem + newExt
            results.append((f.name, newName))
            if not dry_run:
                f.rename(f.parent / newName)
        else:
            results.append((f.name, f.name))
    return results


