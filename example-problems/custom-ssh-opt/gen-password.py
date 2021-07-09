import zlib
import os
import sys


seed = ""

# TODO : read seed
with open("seed", "r") as f:
    seed = f.read()

if seed == "":
    print("Seed was not read from filesystem. Aborting.")
    sys.exit(-1)

# TODO : compute password by crc32 on seed

password = hex(zlib.crc32(seed.encode()))
password = password[2:]


# TODO : write password to file

with open("password", "w") as f:
    f.write(password)



# DONE
sys.exit()
