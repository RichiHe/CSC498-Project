import random
from Elliptic_curve import EllipticPoint


Alphabet = "abcdefghijklmnopqrstuvwxyz01234567890 ,."
def encode_data_to_point(data, curve):
    """Encode data to a point on the curve."""
    # Ensure the data is within the range of valid x-coordinates
    if data < 0 or data >= len(curve.allx):
        # print(data, "out of range")
        raise ValueError("Data is out of range for the given curve.")

    x = curve.allx[data]
    # print(x, "encode valid")
    y_squared = (x**3 + curve.a * x + curve.b) % curve.p

    # Find a y-coordinate corresponding to x
    for possible_y in range(curve.p):
        if (possible_y**2) % curve.p == y_squared:
            return EllipticPoint(x, possible_y)
    raise ValueError("No valid point found for the data.")

def decode_point_to_data(point, curve):
    """Decode a point on the curve back to the original data."""

    if point.x in curve.allx:
        # print(point.x, "decode valid")
        return curve.allx.index(point.x)
    else:
        # print(point.x, "invalid")
        raise ValueError("Point's x-coordinate is not valid for decoding.")



def elgamal_encrypt(curve, generator, public_key, plaintext_numbers):
    plaintext_points = [encode_data_to_point(data, curve) for data in plaintext_numbers]
    ciphertexts = []
    for M in plaintext_points:
        k = random.randint(1, curve.p - 1)  # Choose a random k for each message
        # print("random k is", k)
        A = curve.multiply(generator, k)
        B = curve.add_points(M, curve.multiply(public_key, k))
        ciphertexts.append((A, B))
    return ciphertexts


def elgamal_decrypt(curve, private_key, ciphertexts):
    plaintext_points = []
    for A, B in ciphertexts:
        if A.infinity:
            M = curve.add_points(B, A)
        else:
            S = curve.multiply(A, private_key)  # Shared secret
            possible_y = curve.p - S.y % curve.p
            S_inverse = EllipticPoint(S.x, possible_y)  # Inverse of S
            M = curve.add_points(B, S_inverse)  # Decrypt to get message point
        plaintext_points.append(M)

    plaintext_numbers = [decode_point_to_data(point, curve) for point in plaintext_points]
    return plaintext_numbers

