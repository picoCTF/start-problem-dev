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
    
    cleartext = ""
    with open("password","r") as f:
        cleartext = f.read()
    
    m = ascii2int(cleartext)

    c = pow(m, e, n)
    with open("password.enc" , "w+") as f:
        f.write(str(c))
    
    os.remove('password')
