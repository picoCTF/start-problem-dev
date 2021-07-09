import re
import os
import sys



# TODO : read in flag

flag = ""

with open("flag", "r") as f:
    flag = f.read()

# TODO : get randomized part

if flag == "":
    print("Flag was not read from filesystem. Aborting.")
    sys.exit(-1)
else:
    # Get hash part
    flag_rand = re.search("{.*}$", flag)
    if flag_rand == None:
        print("Flag isn't wrapped by curly braces. Aborting.")
        sys.exit(-2)
    else:
        flag_rand = flag_rand.group()
        flag_rand = flag_rand[1:-1]
        

# TODO : build flag parts by adding in static parts and randomized part

flag_1of3 = "picoCTF{sh311_"
flag_2of3 = "n4v1g4t10n_ftw_"
flag_3of3 = flag_rand + "}"
flag = flag_1of3 + flag_2of3 + flag_3of3


# TODO : write flag parts and flag to file

with open("flag_1of3", "w") as f:
    f.write(flag_1of3)

with open("flag_2of3", "w") as f:
    f.write(flag_2of3)

with open("flag_3of3", "w") as f:
    f.write(flag_3of3)
    
os.remove("flag")
with open("flag", "w") as f:
    f.write(flag)



# DONE
sys.exit()
