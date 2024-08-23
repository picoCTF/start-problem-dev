# rsa_oracle

- Namespace: picoctf
- ID: rsa-oracle
- Type: custom
- Category: Cryptography
- Points: 300
- Templatable: yes

## Description

Can you abuse the oracle?

An attacker was able to intercept communications between a bank and a fintech company. They managed to get the {{url_for('secret.enc', 'message')}} (ciphertext) and the {{url_for('password.enc', 'password')}} that was used to encrypt the message.

## Details

After some intensive reconassainance they found out that the bank has an oracle that was used to encrypt the password and can be found here `nc {{server}} {{port}}`. Decrypt the password and use it to decrypt the message. The oracle can decrypt anything except the password.

## Hints

- Crytography Threat models: chosen plaintext attack.
- OpenSSL can be used to decrypt the message. e.g `openssl enc -aes-256-cbc -d ...`
- The key to getting the flag is by sending a custom message to the server by taking advantage of the RSA encryption algorithm.
- Minimum requirements for a useful cryptosystem is CPA security.

## Challenge Options
```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Solution Overview

- Download password.enc
- Using the oracle, encrypt a small number, say 2
- Calculate the product of the ciphertexts
- Decode the product using the oracle
- Divide the decrypted product by hex of the number used in step 2. In this case we divide with 32 (use https://www.calculator.net/hex-calculator.html)
- Convert the result from hex using cyberchef to get key
- Decrypt the message using openssl `openssl enc -aes-256-cbc -d -in secret.enc -out flag -k replace_this_with_key`

## Learning Objective

Understanding the loopholes in RSA.

## Tags

- browser_webshell_solvable

## Attributes

- author: Geoffrey Njogu
- organization: Cylab Africa
- event: picoCTF 2024
