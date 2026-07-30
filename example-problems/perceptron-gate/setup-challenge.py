################################################################################
# Setup flag and metadata for the challenge
################################################################################
import os, re, json, sys

def main():
    flag_env = os.environ.get("FLAG", "")
    if flag_env == "":
        print("Flag was not read from environment. Aborting.")
        sys.exit(2)

    # Extract the random hex inside {...} from FLAG and normalize to 8 hex chars
    m = re.search(r"{([0-9a-fA-F]+)}$", flag_env)
    if not m:
        print("FLAG must end with {...} random hex. Aborting.")
        sys.exit(3)

    rand = m.group(1).lower().zfill(8)[:8]
    flag = f"academy{{perceptron_party_{rand}}}"

    # Write plaintext flag for the service to read
    with open("flag.txt", "w") as f:
        f.write(flag + "\n")

    # Also store in /challenge/metadata.json for infra
    metadata = {"flag": flag}
    with open("/challenge/metadata.json", "w") as f:
        f.write(json.dumps(metadata))

if __name__ == "__main__":
    main()

