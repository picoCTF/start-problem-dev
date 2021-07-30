################################################################################
# Configure a box for the custom web example challenge.
################################################################################


import sys
import os
import subprocess
import re
import zlib
import json



def main():

    try:
        # Split flag into 3 parts  ============================================
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
        
        with open("/usr/local/apache2/htdocs/public-html/style.css", "a") as f:
            f.write('/* ' + new_flag + ' */')

        # =====================================================================


        # Create and update metadata.json =====================================

        metadata = {}
        metadata['flag'] = str(new_flag)
        json_metadata = json.dumps(metadata)
        
        with open("/challenge/metadata.json", "w") as f:
            f.write(json_metadata)

        # =====================================================================

    except subprocess.CalledProcessError:
        print("A subprocess has returned an error code")
        sys.exit(1)



# =============================================================================


if __name__ == "__main__":
    main()

