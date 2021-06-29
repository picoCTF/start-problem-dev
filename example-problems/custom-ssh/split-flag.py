import re
import os



# TODO : read in flag

flag = ""

with open("flag", "r") as f:
    flag = f.read()

# TODO : get randomized part

if flag == "":
    print("Flag was not read from filesystem. Aborting.")
    return -1
else:
    # Get hash part
    flag_rand = re.search("{.*}$", flag)
    if flag_rand == None:
        print("Flag isn't wrapped by curly braces. Aborting.")
        return -2
    else:
        flag_rand = flag_rand.group()
        flag_rand = flag_rand[1:-1]
        

# TODO : build flag parts by adding in static parts and randomized part

flag_1of3 = "picoCTF{sh311_"
flag_2of3 = "n4v1g4t10n_ftw_"
flag_3of3 = flag_rand + "}"


# TODO : put in env vars

os.environ["FLAG_1OF3"] = flag_1of3
os.environ["FLAG_2OF3"] = flag_2of3
os.environ["FLAG_3OF3"] = flag_3of3



# DONE