import math


class EllipticPoint:
    def __init__(self, x, y, infinity=False):
        self.x = x
        self.y = y
        self.infinity = infinity # Point at infinity

    def __eq__(self, other):
        if self.infinity and other.infinity:
            return True
        if self.infinity or other.infinity:
            return False
        return self.x == other.x and self.y == other.y

    def __str__(self):
        if self.infinity:
            return "Point(infinity)"
        return f"Point({self.x}, {self.y})"


    def __repr__(self):
        if self.infinity:
            return "Point(infinity)"
        return f"({self.x}, {self.y})"


# Define the elliptic curve y^2 = x^3 + ax + b over F_p
class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.allx = self.find_valid_x_coordinates()

    def add_points(self, P, Q):
        # print(P, Q)
        # Handle the identity element (point at infinity)
        if P.infinity:
            return Q
        # print(Q.infinity)
        if Q.infinity:
            return P
        if P == Q:
            return self.double_point(P)
        if P.x == Q.x and P.y != Q.y:
            return EllipticPoint(None, None, infinity=True)  # Point at infinity

        # Slope of the line between P and Q
        m = (Q.y - P.y) * self.modinv(Q.x - P.x, self.p) % self.p

        # Calculate the resulting point R
        x_r = (m**2 - P.x - Q.x) % self.p
        y_r = (m * (P.x - x_r) - P.y) % self.p

        return EllipticPoint(x_r, y_r)

    def double_point(self, P):
        if P.infinity:
            return P

        # Slope of the tangent at point P
        m = (3 * P.x**2 + self.a) * self.modinv(2 * P.y, self.p) % self.p

        # Calculate the resulting point R
        x_r = (m**2 - 2 * P.x) % self.p
        y_r = (m * (P.x - x_r) - P.y) % self.p
        return EllipticPoint(x_r, y_r)

    # def multiply(self, P, times):
    #     if times == 1:
    #         return P
    #
    #     if times == 2:
    #         return self.double_point(P)
    #
    #     half = times // 2
    #     one = times % 2
    #     # print("half", half)
    #     ret = multiples.setdefault((P.base, times),
    #                                self.add_points(self.multiply(P, half),
    #                                                self.multiply(P, half + one)))
    #
    #     return ret

    def multiply(self, P, times):
        # Performs scalar multiplication of a point P by an integer times
        N = EllipticPoint(None, None, True)  # Point at infinity
        Q = P
        while times > 0:
            if times % 2 == 1:
                N = self.add_points(N, Q)
            Q = self.double_point(Q)
            times //= 2
        return N

    def modinv(self, a, m):
        # Compute the modular inverse of a modulo m using the extended Euclidean algorithm
        g, x, _ = self.egcd(a % m, m)
        if g != 1:
            raise Exception('Modular inverse does not exist')
        else:
            return x % m

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def __str__(self):
        return f'y^2 = x^3 + {self.a}x + {self.b}  mod{self.p}'

    def find_valid_x_coordinates(self):
        """Find all x-coordinates for which there are valid points on the curve."""
        valid_x_coords = []
        for x in range(self.p):
            y_squared = (x**3 + self.a * x + self.b) % self.p
            if self.is_quadratic_residue(y_squared):
                valid_x_coords.append(x)
        return valid_x_coords

    def is_quadratic_residue(self, a):
        """Check if 'a' is a quadratic residue modulo 'p'."""
        return pow(a, (self.p - 1) // 2, self.p) == 1




