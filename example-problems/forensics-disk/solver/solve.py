import subprocess

def main():
    # Use subprocess to gunzip the disk file
    subprocess.run(["gunzip", "disk.flag.img.gz"])

    # Open disk file and seek to flag location
    with open("disk.flag.img", "rb") as r:
        r.seek(509014036)
        flag = r.read(29)
        with open("flag", "wb") as w:
            w.write(flag)

if __name__ == "__main__":
    main()