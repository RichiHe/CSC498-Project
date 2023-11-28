from Elliptic_curve import EllipticCurve, EllipticPoint
from ElGamal import *
from Encryptor import encrypt
from Decryptor import decrypt
import random


def Main():
    print("Please enter a, b, and p in the form a, b, p:")
    s = input()
    abp = s.split(",")
    a = int(abp[0])
    b = int(abp[1])
    p = int(abp[2])

    if (4*(a**3) + 27*(b**2)) == 0:
        raise ValueError("Invalid a and b")

    curve = EllipticCurve(a, b, p)

    print("Curve is", curve)
    english = False
    if len(curve.allpoints) > 10:
        english = True

    print("Encrypt enter 1, Decrypt enter 2, Get generator enter 3")
    operation = input()
    if operation == "3":
        print("Valid x are", curve.allpoints, "select a point by index to be the generator")
        generatorindex = int(input())


        generator = curve.allpoints[generatorindex]
        print("enter a private key")
        private = int(input())
        public = curve.multiply(generator, private)
        print("generator, public key =", generator, public)
        return
    elif operation == "1":
        if english:
            print("Input your message(any English words and numebers):")
        else:
            print(f"Input your message(numbers from 0 to {len(curve.allpoints) - 1}):")
        plaintext = input().lower()
        print("Please enter generator and public key, in the form Gen.x, Gen.y, PK.x, PKy")
        gen_pk = input().split(",")
        if gen_pk[0] == "inf":
            gen = EllipticPoint(0, 0, True)
        else:
            gen = EllipticPoint(int(gen_pk[0]), int(gen_pk[1]))

        if "inf" in gen_pk[2]:
            PK = EllipticPoint(None, None, True)
        else:
            PK = EllipticPoint(int(gen_pk[2]), int(gen_pk[3]))
        cipherpoint = encrypt(curve, gen, PK, plaintext, english)
        a = str(cipherpoint)
        a = a.replace("(", "")
        a = a.replace(")", "")
        a = a.replace("[", "")
        a = a.replace("]", "")
        ciphertext = a.replace(",", "")
        print("Encrypted message = ", ciphertext)

        return
    else:
        print("Please enter private key, ciphertext in the form: k, cipher text")
        k_CT = input().split(",")
        private_key = int(k_CT[0])
        ciphertext = k_CT[1]
        if english:
            flag = True
        else:
            flag = False
        print("Message is", decrypt(curve, private_key, ciphertext, flag))


if __name__ == "__main__":
   Main()
