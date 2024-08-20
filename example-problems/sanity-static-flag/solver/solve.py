import subprocess

def main():
    # Copy the flag from the flag file
    with open('./flag.txt', 'r') as r:
        flag = r.read().strip()
        with open('./flag', 'w') as w:
            w.write(flag)

if __name__ == "__main__":
    main()