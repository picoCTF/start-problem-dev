# AGENTS.md

This file is an opinionated, practical playbook for building working picoCTF
challenges with cmgr. It is based on:

- Building with CMGR - Quick Start Guide
- common-errors/duplicate-network.md
- Every tutorial/challenge under example-problems/

Use this as a hands-on checklist. If you follow it top-to-bottom, you should be
able to stand up a working challenge quickly and avoid common cmgr pitfalls.

## 1) Core Mental Model

- cmgr is a Docker wrapper with challenge-specific metadata, templating, and
  orchestration behavior.
- Containers are still normal Docker containers.
- cmgr discovers challenges from a single configured challenge tree
  (`CMGR_DIR`). If your challenge is outside that tree, cmgr will not find it.
- You reference challenges by namespace and ID (for example,
  `picoctf/examples/sanity-download`), not by filesystem path.

## 2) Required Local Setup

1. Install Docker and cmgr.
2. Configure these env vars (commonly in shell profile):
   - `CMGR_DB`
   - `CMGR_DIR`
   - `CMGR_ARTIFACTS_DIR`
3. Keep all challenge folders under `CMGR_DIR`.

Quick health checks:

- `cmgr update` should discover your challenge.
- `cmgr list` should show `namespace/id`.

If discovery fails, the challenge is usually in the wrong directory tree.

## 3) Pick an Archetype First (Copy the Closest Example)

Do this before writing anything: choose the challenge type and start from the
nearest example.

- Static downloadable artifact:
  `example-problems/sanity-static-flag`
- Dynamic downloadable artifact (templated flag injection):
  `example-problems/forensics-grep`
- Complex forensics artifact with anti-cheese considerations:
  `example-problems/forensics-disk`
- Web service challenge:
  `example-problems/web-css`
- Single-container netcat/socat service:
  `example-problems/reversing-python`
- Multi-container service with builder/runtime separation:
  `example-problems/general-ssh`
- Interactive black-box service pattern:
  `example-problems/perceptron-gate`

## 4) Minimal Challenge Contract

Every cmgr challenge must have:

- `Dockerfile`
- `problem.md`
- `/challenge/metadata.json` generated during image build

Most challenges should also have:

- `/challenge/artifacts.tar.gz` if users need downloadable files
- `solver/solve.py` (required in picoCTF authoring workflow)
- `solver/requirements.txt` if solver uses non-stdlib packages

## 5) problem.md Rules That Matter

The first metadata block should include at least:

- `Namespace: picoctf/...`
- `ID: ...`
- `Type: custom`
- `Category: ...`
- `Points: 1` (initially)
- `Templatable: yes|no`
- `MaxUsers: 0|1`

Operational guidance:

- Put artifact download links in Description (Details may be hidden until launch
  for on-demand challenges).
- Use Details for instance-specific connection info.
- Include Solution Overview and hints.
- Keep Challenge Options resource limits minimal but sufficient.

Useful template functions used in examples:

- `{{url_for("file", "link text")}}` for artifacts
- `{{link_as('/', 'text')}}` for web links (single published port)
- `{{link_as('/', 'text', 'port_name')}}` for named published ports
- `{{server}}`, `{{port}}` for default network endpoint
- `{{server("name")}}`, `{{port("name")}}` for named endpoints
- `{{lookup("key")}}` for values stored in `metadata.json`

## 6) Dockerfile Patterns (Copy/Adjust)

### A) Static Artifact Pattern (Sanity)

1. Create `/challenge` with restrictive permissions.
2. Copy files.
3. Package artifacts to `/challenge/artifacts.tar.gz`.
4. Write `/challenge/metadata.json` with accepted flag.

### B) Dynamic Flag Pattern (Forensics Grep/Disk)

1. Add `ARG FLAG` in the challenge stage.
2. Derive your custom flag string from cmgr-provided `FLAG` randomness.
3. Inject flag into artifact at build time.
4. Save the final accepted flag in `/challenge/metadata.json`.

Why this matters: templated flags are critical for anti-cheating and instance
regeneration.

### C) Web Service Pattern (Web CSS)

1. `EXPOSE <port>` in Dockerfile.
2. Add cmgr publish tag exactly as an uppercase comment:
   - `# PUBLISH <port> AS <name>`
3. Reference that endpoint in `problem.md` via `link_as`.

### D) Netcat/Interactive Service Pattern (Reversing/Perceptron)

1. Install service dependencies (for example `socat`, `python3`).
2. Provide `start.sh` that launches listener:
   - `socat tcp-listen:<port>,reuseaddr,fork SYSTEM:"..."`
3. `EXPOSE` and optionally `# PUBLISH` port.
4. Ensure service exits promptly on success, and does not hang forever waiting
   for input.

### E) Multi-Container Pattern (General SSH)

1. Use a `builder` stage to generate secret material and metadata.
2. Use a separate runtime stage for user interaction.
3. Copy only what runtime needs via `COPY --from=builder ...`.
4. Use `# LAUNCH <stage_name>` to select which stage stays running.

This separation reduces accidental metadata exposure on exploitable services.

## 7) Flags, Seeds, and Manual Docker Testing

- cmgr supplies build args like `FLAG` (and often `SEED`) automatically.
- If you run `docker build` manually, you must pass required args yourself:
  - `docker build . --build-arg FLAG='picoCTF{deadbeef}'`
  - Add `--build-arg SEED='1234'` if your build logic needs seed.

Practical recommendation from examples:

- Validate `FLAG` and `SEED` explicitly in Python setup scripts.
- Fail fast with clear errors if missing or malformed.

## 8) cmgr vs Docker Debugging Workflow

Preferred build loop:

1. Build and debug with Docker first (better low-level error output).
2. Then run with cmgr.

Typical sequence:

1. `cmgr update`
2. `cmgr list`
3. `cmgr playtest <namespace/id>`
4. `cmgr test <namespace/id>` (or your team standard test command)

For templating verification, build multiple seeds and compare generated flags
using `cmgr` system dump tooling (as shown in forensics-grep walkthrough).

## 9) Critical Gotchas (Do Not Skip)

### Challenge discovery and naming

- Problem not found after `cmgr update`: challenge likely not under `CMGR_DIR`
  tree.
- Playtest target is `namespace/id`, not folder path.

### PUBLISH/port issues

- `PUBLISH ... AS ...` is a cmgr comment tag, not Docker syntax.
- Keep it commented and uppercase (`PUBLISH` + `AS`).
- If you name a published port, use the same name in `problem.md` templates.

### Missing required challenge artifacts

- No `/challenge/metadata.json` => challenge is invalid.
- If `problem.md` references downloadable files, ensure they are included in
  `/challenge/artifacts.tar.gz`.

### Docker/cmgr state mismatch (duplicate networks)

Symptom:

- cmgr errors that `network with name cmgr-<n> already exists`.

Cause:

- Docker restored old networks/containers while cmgr state differs.

Fix (careful if you run other Docker projects):

1. Stop stale containers.
2. Prune stale networks.
3. Run `cmgr update` again.

### Build-step path errors

- Verify paths in `RUN` commands against actual `WORKDIR` and `COPY` targets.
- Classic failure from examples: executing setup script from a path where it was
  never copied.

### Service liveness and resource hygiene

- Interactive services should not block forever.
- Exit after flag output.
- Set minimal challenge options in `problem.md` and increase only if required.

### Anti-cheese checks for artifact-heavy problems

- Test whether raw artifacts leak flags via `strings`/`grep`.
- If needed, obfuscate or encode flag placement to preserve intended learning
  objective.

## 10) Pre-Submission Checklist

1. Challenge builds cleanly in Docker with explicit build args.
2. Challenge is discovered by `cmgr update` from `CMGR_DIR` tree.
3. `cmgr playtest <namespace/id>` launches successfully.
4. Incorrect flag is rejected.
5. Correct flag is accepted.
6. Intended path to solve works from player-visible materials.
7. `problem.md` metadata, details, hints, and Solution Overview are complete.
8. Port tags (`PUBLISH`) and problem templates (`link_as`, `port`, `server`) are
   aligned.
9. Solver script works and writes recovered flag to `./flag`.
10. If templated, verify multiple generated instances produce different flags and
    remain solvable.

## 11) Quick Start Authoring Recipe

When creating a new challenge quickly:

1. Copy the closest archetype folder from `example-problems/`.
2. Rename folder and update `problem.md` (`Namespace`, `ID`, text).
3. Replace challenge logic/artifacts.
4. Ensure Dockerfile generates `/challenge/metadata.json`.
5. If web/service challenge, ensure `EXPOSE` + correct `# PUBLISH` tag and
   matching `problem.md` references.
6. Run Docker build manually with `--build-arg FLAG=...` first.
7. Move/copy challenge into `CMGR_DIR` tree.
8. Run `cmgr update`, then `cmgr playtest namespace/id`.
9. Validate wrong/correct flag handling.
10. Finalize a solver script and clean problem wording.

If you follow this recipe, you avoid nearly all first-time cmgr failures seen in
the training examples.