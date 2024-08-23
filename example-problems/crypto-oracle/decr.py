# RSA encryption and decrytion
from helper import *

if __name__ == "__main__":
    print("*****************************************")
    print("****************THE ORACLE***************")
    print("*****************************************")

    keysize = 256 
    p = 78615231505791119778531679171954912116516772172405580837835038280745008520119
    q = 70057651003046527661678151293247823379678754249928504243640950278981509215109
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    d = int(modinv(e, phi))


    with open("../password.enc", "r") as f:
        secret = f.read()

    try:
        request = input("what should we do for you? \nE --> encrypt D --> decrypt. \n" ).upper()
        while(request):
            if (request == 'E'):
                cleartext = input("enter text to encrypt (encoded length must be less than keysize): ")
                print(f"{cleartext}")
                m = ascii2int(cleartext)
                print("\nencoded cleartext as Hex m: %s" % format(m, 'x'))

                c = pow(m, e, n)
                print(f"\nciphertext (m ^ e mod n) {c}")

            elif (request =='D'):
                ciphertext = int(input("Enter text to decrypt: "))

                
                if(secret == str(ciphertext)):
                    print("Lol, good try, can't decrypt that for you. Be creative and good luck")
                else:
                    newclearint = pow(ciphertext, d, n)
                    print("decrypted ciphertext as hex (c ^ d mod n): %s" % format(newclearint, 'x'))
                    print("decrypted ciphertext: %s" % int2ascii(newclearint))
                

            request = input("\nwhat should we do for you? \nE --> encrypt D --> decrypt. \n" ).upper()


    except:
        KeyboardInterrupt
    