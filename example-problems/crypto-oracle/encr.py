import os
import re
from helper import *


if __name__ == "__main__":
    keysize = 256 
    p = 78615231505791119778531679171954912116516772172405580837835038280745008520119
    q = 70057651003046527661678151293247823379678754249928504243640950278981509215109
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = int(modinv(e, phi))
    
    #password has a lenght of 5
    flag = os.environ.get('FLAG')
    flag_rand = re.search("{.*}$", str(flag))
    flag_rand = flag_rand.group()
    flag_rand = flag_rand[1:-1]
    flag_rand = flag_rand.zfill(8)
    cleartext = flag_rand[:-3]
    
    m = ascii2int(cleartext)

    c = pow(m, e, n)
    with open("password.enc" , "w+") as f:
        f.write(str(c))
