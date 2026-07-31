#!/usr/bin/env python3
import base64
import csv
import datetime
import json
import os
import random
import re
import string
import tarfile
from pathlib import Path


def derive_flag(cmgr_flag: str) -> str:
    m = re.fullmatch(r"[^{}]*\{([^{}]+)\}", cmgr_flag.strip())
    if not m:
        raise ValueError("FLAG build arg is malformed")
    return f"academy{{triage_then_decode_{m.group(1)}}}"


def chunk_text(value: str, n: int) -> list[str]:
    return [value[i : i + n] for i in range(0, len(value), n)]


def random_chunk(rng: random.Random, n: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits + "+/="
    return "".join(rng.choice(alphabet) for _ in range(n))


def main() -> None:
    import sys

    if len(sys.argv) != 2:
        raise ValueError("usage: build-challenge.py <FLAG>")

    cmgr_flag = sys.argv[1]
    final_flag = derive_flag(cmgr_flag)

    rng = random.Random(final_flag)
    encoded_flag = base64.b64encode(final_flag.encode()).decode()
    real_chunks = chunk_text(encoded_flag, 6)

    app_dir = Path(os.environ.get("APP_DIR", "/app"))
    challenge_dir = Path(os.environ.get("CHALLENGE_DIR", "/challenge"))
    app_dir.mkdir(parents=True, exist_ok=True)
    challenge_dir.mkdir(parents=True, exist_ok=True)

    artifact_root = app_dir / "triage-bundle"
    artifact_root.mkdir(parents=True, exist_ok=True)

    real_ids = [f"EXP-{rng.randint(1000, 9999)}" for _ in real_chunks]

    rows: list[tuple[str, str]] = []
    for exp_id, chunk in zip(real_ids, real_chunks):
        rows.append((exp_id, chunk))

    for _ in range(len(real_chunks) * 3):
        rows.append((f"EXP-{rng.randint(1000, 9999)}", random_chunk(rng)))

    rng.shuffle(rows)
    with (artifact_root / "export-map.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["export_id", "chunk"])
        writer.writerows(rows)

    start = datetime.datetime(2026, 1, 10, 8, 0, 0)
    statuses = [200, 200, 200, 304, 404, 500, 503]
    request_lines = []

    for i in range(110):
        ts = start + datetime.timedelta(seconds=i)
        status = rng.choice(statuses)
        req_id = f"REQ-{rng.randint(10000, 99999)}"
        path = rng.choice([
            "/health",
            "/api/v1/users",
            "/api/v1/session",
            "/api/v1/export/ping",
            "/api/v1/jobs",
        ])
        request_lines.append(
            f"{ts.isoformat()}Z {req_id} {status} GET {path}"
        )

    insert_positions = sorted(rng.sample(range(20, 95), len(real_ids)))
    for idx, exp_id in zip(insert_positions, real_ids):
        ts = start + datetime.timedelta(seconds=idx)
        req_id = f"REQ-{rng.randint(10000, 99999)}"
        line = f"{ts.isoformat()}Z {req_id} 418 GET /api/v1/export/{exp_id}"
        request_lines[idx] = line

    (artifact_root / "requests.log").write_text("\n".join(request_lines) + "\n")

    (artifact_root / "README.txt").write_text(
        "Ops dropped this triage bundle after an incident.\n"
        "Only one sequence of export IDs is meaningful.\n"
        "Find suspicious requests in requests.log and pivot through export-map.csv.\n"
    )

    bundle_path = app_dir / "triage-bundle.tar.gz"
    with tarfile.open(bundle_path, "w:gz") as tar:
        tar.add(artifact_root, arcname="triage-bundle")

    with tarfile.open(challenge_dir / "artifacts.tar.gz", "w:gz") as tar:
        tar.add(bundle_path, arcname="triage-bundle.tar.gz")

    (challenge_dir / "metadata.json").write_text(json.dumps({"flag": final_flag}) + "\n")


if __name__ == "__main__":
    main()
