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
        flag_rand = re.search("{.*}$", flag)
        if flag_rand == None:
            print("Flag isn't wrapped by curly braces. Aborting.")
            sys.exit(-2)
        else:
            flag_rand = flag_rand.group()
            flag_rand = flag_rand[1:-1]

    new_flag = "picoCTF{1n5p3t0r_ftw_" + flag_rand + "}"
    
    with open("/usr/share/nginx/html/style.css", "a") as f:
        f.write('/* ' + new_flag + ' */')

    # =====================================================================


    # Create and update metadata.json =====================================

    metadata = {}
    metadata['flag'] = str(new_flag)
    json_metadata = json.dumps(metadata)
    
    with open("metadata.json", "w") as f:
        f.write(json_metadata)

    # =====================================================================


# =============================================================================


if __name__ == "__main__":
    main()

