################################################################################
# Setup flag and metadata for the challenge
################################################################################

import sys
import subprocess
import os
import re
import json

def main():

  try:
    
    # Craft flag ==========================================================
    flag = os.environ.get("FLAG")

    if flag == "":
      print("Flag was not read from environment. Aborting.")
      sys.exit(2)
    else:
      # Get hash part
      flag_rand = re.search("{.*}$", flag)
      if flag_rand == None:
        print("Flag isn't wrapped by curly braces. Aborting.")
        sys.exit(3)
      else:
        flag_rand = flag_rand.group()
        flag_rand = flag_rand[1:-1]
        flag_rand = flag_rand.zfill(8)

    flag = "picoCTF{4_d14m0nd_1n_7h3_r0ugh_" + flag_rand + "}"
    open('flag.txt', 'w').write(flag)

    # =====================================================================

    # Create and update metadata.json =====================================

    metadata = {}
    metadata['flag'] = str(flag)
    json_metadata = json.dumps(metadata)

    with open("/challenge/metadata.json", "w") as f:
      f.write(json_metadata)

    # =====================================================================

  except subprocess.CalledProcessError:
    print("A subprocess got an error")
    sys.exit(1)

# =============================================================================

if __name__ == "__main__":
  main()
