from pwn import *

def main():
    # Connect to server
    conn = remote("challenge", 5555)

    # Send payload
    conn.sendline(b"win")

    # Exit
    conn.sendline(b"exit")

    # Receive all
    response = conn.recvall()

    # Convert response to ASCII
    response = response.decode()

    # Get ASCII hex string of numbers from response
    numbers = response.split(" ")[7:-8]

    flag=""
    for num in numbers:
        flag += chr(int(num, 16))

    # Write flag to file
    with open("./flag", "w") as w:
        w.write(flag)

if __name__ == "__main__":
    main()