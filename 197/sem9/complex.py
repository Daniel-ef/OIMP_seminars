class ComplexException(BaseException):
    def __init__(self, complex, other):
        self.arg1 = complex
        self.arg2 = other


class Complex:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __str__(self) -> str:
        return '{}{}{}i'.format(
            self.re,
            '+' if self.im >= 0 else '',
            self.im
        )

    def __add__(self, other):
        return self.__class__(
            self.re + other.re,
            self.im + other.im
        )

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__class__(self.re * other, self.im * other)
        elif isinstance(other, Complex):
            return self.__class__(
                self.re * other.re - self.im * other.im,
                self.re * other.im + self.im * other.re
            )
        else:
            raise ComplexException(self.__str__(), other)

    __rmul__ = __mul__


if __name__ == '__main__':

    [].__str__() # str([])

    cmplx1 = Complex(5, -4)
    cmplx2 = Complex(3, 5)


    print(cmplx1, cmplx2)
    print('+', cmplx1 + cmplx1)
    print('*', cmplx1 * cmplx1)

    print('* const', cmplx1 * 5)
    print('const *', 5 * cmplx1)

    print("Exceptions\n")
    try:
        print(cmplx1 * 'str')
    except ComplexException as exc:
        print("Error:", exc.arg1, exc.arg2)
    else:
        print('Ok')

    # try:
    #     5 / 0
    # except ZeroDivisionError:
    #     print("Dont do it")