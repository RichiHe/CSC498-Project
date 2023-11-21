from ElGamal import elgamal_encrypt, Alphabet
def encrypt(curve, generator, public_key, plaintext, flag):
    if flag:
        transform = ""
        for c in plaintext:
            transform += str(Alphabet.index(c))
            transform += " "
    else:
        transform = plaintext

    datas = []
    for e in transform:
        if e == " ":
            datas.append(10)
        else:
            datas.append(int(e))

    return elgamal_encrypt(curve, generator, public_key, datas)
