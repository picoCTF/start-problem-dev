
def main():
    # Read text from the problem artifact
    with open("./war-and-peace.flag.txt", "r") as r:
        # Search for flag in lines
        for line in r:
            if "picoCTF" in line:
                print(line)
                with open("./flag", "w") as w:
                    w.write(line)
                    break

if __name__ == "__main__":
    main()