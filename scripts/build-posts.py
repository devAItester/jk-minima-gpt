#!/usr/bin/env python3

from pathlib import Path
import json
import re
import shutil
import subprocess

SOURCE = Path("posts")
TARGET = Path("_posts")

if not SOURCE.exists():
    raise SystemExit("posts/ does not exist")

if TARGET.exists():
    shutil.rmtree(TARGET)
TARGET.mkdir()

def first_commit(path: Path) -> str:
    result = subprocess.run(
        ["git", "log", "--reverse", "--format=%cI", "--", str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    values = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    if not values:
        raise SystemExit(f"Cannot determine creation time for {path}")
    return values[0]

def slugify(title: str) -> str:
    value = title.strip().lower()
    value = re.sub(r"[^\w]+", "-", value, flags=re.UNICODE)
    value = value.strip("-_")
    if not value:
        raise SystemExit(f"Cannot derive slug from filename: {title}")
    return value

files = sorted(SOURCE.glob("*.md"))
seen = set()

for source in files:
    title = source.stem
    created = first_commit(source)
    date = created[:10]
    slug = slugify(title)
    target = TARGET / f"{date}-{slug}.md"

    if target.name in seen or target.exists():
        raise SystemExit(
            f"Two posts would generate the same Jekyll filename: {target.name}"
        )
    seen.add(target.name)

    front_matter = (
        "---\n"
        "layout: post\n"
        f"title: {json.dumps(title, ensure_ascii=False)}\n"
        f"date: {json.dumps(created)}\n"
        "permalink: /posts/:title/\n"
        "---\n\n"
    )

    target.write_text(
        front_matter + source.read_text(encoding="utf-8"),
        encoding="utf-8",
    )

print(f"Prepared {len(files)} posts.")
