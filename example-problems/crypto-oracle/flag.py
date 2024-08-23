################################################################################
# Configure a box for the custom web example challenge.
################################################################################


import sys
import os
import re
import json


def main():

    # picofy flag and append to stylesheet ================================
    flag = os.environ.get("FLAG")

    if flag == "":
        print("Flag was not read from environment. Aborting.")
        sys.exit(-1)
    else:
        # Get hash part
        flag_rand = re.search("{.*}$", str(flag))
        if flag_rand == None:
            print("Flag isn't wrapped by curly braces. Aborting.")
            sys.exit(-2)
        else:
            flag_rand = flag_rand.group()
            flag_rand = flag_rand[1:-1]
            flag_rand = flag_rand.zfill(8)

    new_flag = "picoCTF{su((3ss_(r@ck1ng_r3@_" + flag_rand + "}"

    password=flag_rand[:-3]

    with open("plaintext","w+") as f:
        f.write(new_flag)
    
    
   
    # print(f"the password is {password}")
    cmd = 'openssl enc -aes-256-cbc -salt -in plaintext -out secret.enc -k '+password
    os.system(cmd)

    os.remove('plaintext')
    
    #==============================================
    os.environ['PASSWORD']=str(password)
        

    # =====================================================================


    # Create and update metadata.json =====================================

    metadata = {}
    metadata['flag'] = str(new_flag)
    json_metadata = json.dumps(metadata)
    
    with open("/challenge/metadata.json", "w") as f:
        f.write(json_metadata)

    # =====================================================================


# =============================================================================


if __name__ == "__main__":
    main()
