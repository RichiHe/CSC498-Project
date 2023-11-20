from Elliptic_curve import EllipticCurve, EllipticPoint
from ElGamal import *
import random

if __name__ == "__main__":
    print("hello, please enter a, b, and p(>= 33) in the form a, b, p:")
    s = input()
    abp = s.split(",")
    a = int(abp[0])
    b = int(abp[1])
    p = int(abp[2])
    curve = EllipticCurve(a, b, p)

    #
    # R = curve.add_points(P, Q)
    # R5 = curve.multiply(P, 115)
    # print(R)
    # print(R5)
    # print(multiples)
    print("valid x are", curve.allx, "select one to be the generator")
    generatorx = int(input())
    if generatorx not in curve.allx:
        raise ValueError("Not valid x")
    generator = encode_data_to_point(curve, generatorx)

    print("select a public key")
    private_key = int(input())
    public_key = curve.multiply(generator, private_key)
    print("input your message:")

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
