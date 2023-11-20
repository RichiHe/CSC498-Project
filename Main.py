from Elliptic_curve import EllipticCurve, EllipticPoint
from Elliptic_curve import multiples
from ElGamal import *
import random

if __name__ == "__main__":
    print("hello")
    curve = EllipticCurve(a=2, b=2, p=17)
    P = EllipticPoint(5, 1, (5,1))
    Q = EllipticPoint(3, 1, (3,1))

    R = curve.add_points(P, Q)
    R5 = curve.multiply(P, 115)
    print(R)
    print(R5)
    # print(multiples)
    private_key = 6
    public_key = curve.multiply(P, private_key)
    print("valid is", curve.allx)
    plaintext_numbers = [random.randint(0, len(curve.allx) - 1) for _ in range(3)]
    print("plaintext number is", plaintext_numbers)
    # Encryption
    ciphertexts = elgamal_encrypt(curve, P, public_key, plaintext_numbers)
    cipher_numbers = [point for point in ciphertexts]
    # Encryption
    print("ciphertexts:", ciphertexts)

    # Decryption
    decrypted_numbers = elgamal_decrypt(curve, private_key, ciphertexts)
    print("Decrypted numbers:", decrypted_numbers)
