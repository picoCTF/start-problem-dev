#!/usr/bin/env python3
import base64
import csv
import re
import tarfile
from pathlib import Path


def extract_bundle() -> Path:
    outer = Path("triage-bundle.tar.gz")
    with tarfile.open(outer, "r:gz") as tar:
        tar.extractall(".")
    return Path("triage-bundle")


def collect_ids(requests_log: Path) -> list[str]:
    ids = []
    pattern = re.compile(r"/api/v1/export/(EXP-\d+)$")
    for line in requests_log.read_text().splitlines():
        if " 418 GET " not in line:
            continue
        match = pattern.search(line)
        if match:
            ids.append(match.group(1))
    return ids


def load_map(csv_path: Path) -> dict[str, str]:
    with csv_path.open(newline="") as f:
        reader = csv.DictReader(f)
        return {row["export_id"]: row["chunk"] for row in reader}


def main() -> None:
    bundle = extract_bundle()
    ids = collect_ids(bundle / "requests.log")
    chunk_map = load_map(bundle / "export-map.csv")

    encoded = "".join(chunk_map[exp_id] for exp_id in ids)
    flag = base64.b64decode(encoded).decode()

    with open("flag", "w") as f:
        f.write(flag)


if __name__ == "__main__":
    main()
