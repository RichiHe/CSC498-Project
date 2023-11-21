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
    if len(curve.allx) > 10:
        english = True

    #
    # R = curve.add_points(P, Q)
    # R5 = curve.multiply(P, 115)
    # print(R)
    # print(R5)
    # print(multiples)
    print("Encrypt enter 1, Decrypt enter 2, Get generator enter 3")
    operation = input()
    if operation == "3":
        print("Valid x are", curve.allx, "select a x by index to be the generator")
        generatorx = int(input())


        generator = encode_data_to_point(generatorx, curve)
        print("enter a private key")
        private = int(input())
        public = curve.multiply(generator, private)
        print("generator, public key =", generator, public)
        return
    elif operation == "1":
        if english:
            print("Input your message(any English words and numebers):")
        else:
            print(f"Input your message(numbers from 0 to {len(curve.allx)-1}):")
        plaintext = input().lower()
        print("Please enter generator and public key, in the form Gen.x, Gen.y, PK.x, PKy")
        gen_pk = input().split(",")
        gen = EllipticPoint(int(gen_pk[0]), int(gen_pk[1]))
        PK = EllipticPoint(int(gen_pk[2]), int(gen_pk[3]))
        cipherpoint = encrypt(curve, gen, PK, plaintext, english)
        a = str(cipherpoint)
        a = a.replace("(", "")
        a = a.replace(")", "")
        a = a.replace("[", "")
        a = a.replace("]", "")
        ciphertext = a = a.replace(",", "")
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


    # plaintext_numbers = [random.randint(0, len(curve.allx) - 1) for _ in range(3)]
    # print("plaintext number is", plaintext_numbers)
    # # Encryption
    # ciphertexts = elgamal_encrypt(curve, P, public_key, plaintext_numbers)
    # cipher_numbers = [point for point in ciphertexts]
    # # Encryption
    # print("ciphertexts:", ciphertexts)
    #
    # # Decryption
    # decrypted_numbers = elgamal_decrypt(curve, private_key, ciphertexts)
    # print("Decrypted numbers:", decrypted_numbers)
    #
    #
    # for num in range(len(curve.allx)):
    #     enc = elgamal_encrypt(curve, P, public_key, [num])
    #     ans = elgamal_decrypt(curve, private_key, enc)
    #     print(num, "->", ans[0])

if __name__ == "__main__":
   Main()
