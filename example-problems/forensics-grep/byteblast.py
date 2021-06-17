
import sys



# Process cmdline params
if len(sys.argv) != 4:
   print( "Usage: python3 "+ sys.argv[0] +" (target_file) (payload_file) " + \
           "(target_offset)" )
   sys.exit(1)

target_file = sys.argv[1]
payload_file = sys.argv[2]
target_offset = int(sys.argv[3])


payload = open(payload_file, 'r').read().encode()
# NOTE : ^--- this is brief but does not explicitly close `ende` file


with open(target_file, "r+b") as blob:
    blob.read(target_offset)
    blob.write(payload)



print("Done.")
sys.exit(0)

