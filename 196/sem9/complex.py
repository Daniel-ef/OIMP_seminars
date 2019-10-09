class ComplexError(BaseException):
    def __init__(self, Complex, other):
        self.arg1 = Complex
        self.arg2 = other


class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self) -> str:
        return "{}{}{}i".format(
            self.re,
            "+" if self.im >= 0 else "",
            self.im
        )

    def __add__(self, other):
        return Complex(
            re=self.re + other.re,
            im=self.im + other.im
        )

    def __mul__(self, other):  # a.__mul__(b)
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re * other, self.im * other)
        elif isinstance(other, Complex):
            return Complex(
                self.re * other.re - self.im * other.im,
                self.im * other.re + self.re * other.im
            )
        else:
            raise ComplexError(self.__str__(), other)

    __rmul__ = __mul__  # b.__mul__(a)


cmplx1 = Complex(3, 2)
cmplx2 = Complex(5)
cmplx3 = Complex(10, -2)

"asdf".__str__()  # str("asdf")

print(cmplx1)
print(cmplx2)
print(cmplx3)

print("sum: ", cmplx1 + cmplx3)
print("multiple: ", cmplx1 * cmplx3)
print("multiple1: ", cmplx1 * 3)
print("multiple2: ", cmplx1 * 3.5)
print("multiple3: ", 3 * cmplx1)  # without rmul raise exception

try:
    print(cmplx3 * 'str')
except ComplexError as exc:
    print("Error in multipling complex",
          exc.arg1, exc.arg2)

