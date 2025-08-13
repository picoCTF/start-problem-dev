from pwn import *
import json

def main():
    # Load JSON file into dictionary
    data = json.loads(open("metadata.json").read())

    # Connect to SSH server
    s = ssh("ctf-player", "ssh_host", password=data["password"])
    flag = s('cat drop-in/1of3.flag.txt && cat /2of3.flag.txt && cat 3of3.flag.txt').decode()

    # Write flag to file
    with open("flag", "w") as w:
        w.write(flag)

if __name__ == "__main__":
    main()