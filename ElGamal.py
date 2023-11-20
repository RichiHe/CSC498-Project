import random
from Elliptic_curve import EllipticPoint

def encode_data_to_point(data, curve):
    """Encode data to a point on the curve."""
    # Ensure the data is within the range of valid x-coordinates
    if data < 0 or data >= len(curve.allx):
        raise ValueError("Data is out of range for the given curve.")

    x = curve.allx[data]
    y_squared = (x**3 + curve.a * x + curve.b) % curve.p

    # Find a y-coordinate corresponding to x
    for possible_y in range(curve.p):
        if (possible_y**2) % curve.p == y_squared:
            return EllipticPoint(x, possible_y, (x, possible_y))
    raise ValueError("No valid point found for the data.")

def decode_point_to_data(point, curve):
    """Decode a point on the curve back to the original data."""
    if point.x in curve.allx:
        return curve.allx.index(point.x)
    else:
        raise ValueError("Point's x-coordinate is not valid for decoding.")



def elgamal_encrypt(curve, generator, public_key, plaintext_numbers):
    plaintext_points = [encode_data_to_point(data, curve) for data in plaintext_numbers]
    ciphertexts = []
    for M in plaintext_points:
        k = random.randint(1, curve.p - 1)  # Choose a random k for each message
        A = curve.multiply(generator, k)
        B = curve.add_points(M, curve.multiply(public_key, k))
        ciphertexts.append((A, B))
    return ciphertexts

def elgamal_decrypt(curve, private_key, ciphertexts):
    plaintext_points = []
    for A, B in ciphertexts:
        S = curve.multiply(A, private_key)  # Shared secret
        S_inverse = EllipticPoint(S.x, -S.y % curve.p, (S.x, -S.y % curve.p))  # Inverse of S
        M = curve.add_points(B, S_inverse)  # Decrypt to get message point
        plaintext_points.append(M)

    plaintext_numbers = [decode_point_to_data(point, curve) for point in plaintext_points]
    return plaintext_numbers

