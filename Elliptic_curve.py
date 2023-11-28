import math


class EllipticPoint:
    def __init__(self, x, y, infinity=False):
        if x == "inf":
            self.infinity = True
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
        return self.__repr__()


    def __repr__(self):
        if self.infinity:
            return "(inf, inf)"
        return f"({self.x}, {self.y})"


# Define the elliptic curve y^2 = x^3 + ax + b over F_p
class EllipticCurve:
    a:int
    b:int
    p:int
    allpoints: list
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.allpoints = self.find_valid_points()

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
        # print(P)
        if P.infinity:
            return P

        # Slope of the tangent at point P
        if P.y == 0:
            return EllipticPoint(None, None, True)
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
        # print(P, times)
        if P.infinity:
            return P
        # Performs scalar multiplication of a point P by an integer times
        N = EllipticPoint(None, None, True)  # Point at infinity
        Q = P
        while times > 0:
            if times % 2 == 1:
                N = self.add_points(N, Q)
            Q = self.double_point(Q)
            # print("Q", Q)
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
        return f'y^2 = x^3 + {self.a}x + {self.b}  mod {self.p}'

    def find_valid_points(self):
        """Find all valid points on the elliptic curve."""
        valid_points = []
        for x in range(self.p):
            y_squared = (x**3 + self.a * x + self.b) % self.p
            # if x == 16:
            #     print("ysq", y_squared)
            if self.is_quadratic_residue(y_squared):
                # Find the y-coordinates that correspond to this x-coordinate
                y = self.sqrt_mod_p(y_squared)
                newpoint = EllipticPoint(x, y)
                valid_points.append(newpoint)
                if y != 0:  # If y is not zero, add the symmetric point

                    valid_points.append(EllipticPoint(x, self.p - y))
        return valid_points

    def is_quadratic_residue(self, a):
        """Check if 'a' is a quadratic residue modulo 'p'."""
        if a == 0:
            return True
        return pow(a, (self.p - 1) // 2, self.p) == 1

    def sqrt_mod_p(self, a):
        """Find a square root of 'a' modulo 'p'. Assumes 'a' is a quadratic residue."""
        # This is a simple implementation; in practice, more efficient algorithms are used.
        for possible_y in range(self.p):
            if (possible_y**2) % self.p == a:
                return possible_y
        return None  # This should never happen if 'a' is a quadratic residue

    def findindex(self, p: EllipticPoint):
        for i in range(len(self.allpoints)):
            if self.allpoints[i] == p:
                return i
        return None



