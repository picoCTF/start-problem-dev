import zlib
import os


seed = ""

# TODO : read seed
with open("seed", "r") as f:
    seed = f.read()

if seed == "":
    print("Seed was not read from filesystem. Aborting.")
    return -1

# TODO : compute password by crc32 on seed

password = hex(zlib.crc32(seed.encode()))


# TODO : put in environment var

os.environ['PASSWORD'] = password


# DONE