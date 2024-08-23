from pwn import *
import subprocess

def main():
    two_cipher = "4707619883686427763240856106433203231481313994680729548861877810439954027216515481620077982254465432294427487895036699854948548980054737181231034760249505"
    pw_cipher = open("password.enc", "r").read().strip()
    prod_cipher = str(int(two_cipher) * int(pw_cipher))

    r = remote("challenge", 4242)

    # Choose "D" to decrypt
    r.sendline(b"D")

    # Send the product of the two ciphers
    r.sendline(prod_cipher.encode())

    line = ""
    # Receive output from server
    for _ in range(1, 7):
        line = r.recvline().decode()
    
    # Get decoded hex from line
    prod_dec = line.split(":")[2].strip()

    # Divide the decrypted product by the known plaintext
    pw_hex = hex(int(prod_dec, 16) // 0x32)

    # Convert the hex to ascii
    pw = bytes.fromhex(pw_hex[2:]).decode()

    # Decrypt the flag
    cmd = f"openssl enc -d -aes-256-cbc -in secret.enc -out flag -k {pw}"
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    main()