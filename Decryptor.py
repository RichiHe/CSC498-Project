from ElGamal import elgamal_decrypt, Alphabet
from Elliptic_curve import EllipticPoint


def text_to_point(cipher_text):
    cipher_text += " "
    ret = []
    xy = []
    AB = []
    accu = ""
    for c in cipher_text:
        # print(accu)
        if c == ",":
            continue
        if c == " ":
            if accu != "":
                if accu != "inf":
                    xy.append(int(accu))
                else:
                    xy.append(accu)
                accu = ""
        else:
            accu += c
        if len(xy) == 2:
            if xy[0] == "inf":
                newP = EllipticPoint(None, None, True)
            else:
                newP = EllipticPoint(xy[0], xy[1])
            AB.append(newP)
            xy = []
        if len(AB) == 2:
            ret.append((AB[0], AB[1]))
            AB = []

    return ret



def decrypt(curve, private_key, cipher_text, flag):
    cipher_point = text_to_point(cipher_text)
    datas = elgamal_decrypt(curve, private_key, cipher_point)
    plaintext = ""
    if not flag:
        for e in datas:
            plaintext += str(e)
    else:
        accu = ""
        for e in datas:
            if e == 10:
                plaintext += Alphabet[int(accu)]
                accu = ""
            else:
                accu += str(e)

    return plaintext
