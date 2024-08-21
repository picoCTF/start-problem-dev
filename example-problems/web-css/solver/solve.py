import requests
import re

def main():
    # Connect to web server and download style.css
    r = requests.get("http://challenge:80/style.css")

    # Get response body
    response = r.text

    # Create regex pattern to search for flag
    pattern = "picoCTF{.*}"

    # Search for flag in response
    flag = re.search(pattern, response)

    # Write flag to file
    with open("./flag", "w") as w:
        w.write(flag.group(0))

if __name__ == "__main__":
    main()