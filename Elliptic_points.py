multiples = {}


class Elliptic_point:

    def __init__(self, x, y, a, b, base):
        self._x = x
        self._y = y
        self._a = a
        self._b = b
        self._base = base

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def addpoint(self, other):
        # print("adding")
        if type(other) == infinite_point:
            return self

        if self._x == other.get_x() and self._y == (-1 * other.get_y()):
            return infinite_point(0, 0, self._a, self._b, (0, 0))

        if self == other:
            # print("adding same point")
            ret = multiples.setdefault((self._base, 2), self.multiple(2))
            return ret

        m = (self._x - other.get_x()) / (self._y - other.get_y())
        return self.getR2(self._x, self._y, other.get_x(), m)

    def multiple(self, times):
        print("times", times)
        if times == 1:
            return self

        if times == 2:
            # print("mul2")
            m = 3 * (self._x ** 2) + self._a
            m /= 2 * self._y
            ret = multiples.setdefault((self._base, times),
                                       self.getR1(self._x, self._y, self._x, m))
            return ret

        half = times // 2
        print("half", half)
        ret = multiples.setdefault((self._base, times),
                                   self.multiple(half).addpoint(
                                       self.multiple(half + times % 2)))

        return ret

    def multiple2(self, times):
        i = 1
        ret = self
        while i < times:
            print(i)
            if ret == self:
                print("same")
            ret = ret.addpoint(self)
            i += 1

        return ret


    def getR1(self, xp, yp, xq, m):
        x = m ** 2 - xp - xq
        a = xp - x
        y = m * a - yp
        return Elliptic_point(x, y, self._a, self._b, self._base)


    def getR2(self, xp, yp, xq, m):
        x = m ** 2 - xp - xq
        a = xp - x
        y = m * a - yp
        return Elliptic_point(x, y, self._a, self._b, (x, y))

    def __eq__(self, other):
        if type(other) != Elliptic_point:
            return False

        if self._x == other.get_x() and self._y == other.get_y():
            return True

        return False

    def __str__(self):
        return str((self._x, self._y))


class infinite_point(Elliptic_point):

    def __init__(self, x, y, a, b, base):
        super().__init__(0, 0, a, b, (0, 0))

    def __str__(self):
        return "infinite point"
