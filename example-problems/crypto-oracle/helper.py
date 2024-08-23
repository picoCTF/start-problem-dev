def ascii2int(string):
    textint = 0
    for char in string:
        textint = textint * 256 + ord(char)
    return(textint)

def int2ascii(integer):
    newtext = ""
    while integer > 0:
        currentchar = integer % 256
        newtext = chr(currentchar) + newtext
        integer -= currentchar
        integer = integer // 256
    return(newtext)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m