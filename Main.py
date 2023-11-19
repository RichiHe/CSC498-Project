from Elliptic_points import Elliptic_point
from Elliptic_points import multiples

if __name__ == "__main__":
    print("hello")
    a = Elliptic_point(0, 1, 1, 1, (0,1))
    print(a.multiple(3))
    print(a.multiple2(3))
    print(multiples)
