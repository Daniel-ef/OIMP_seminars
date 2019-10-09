from main import Complex


class Point(Complex):
    def lenght(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __str__(self):
        return "({},{})".format(self.re, self.im)


print('\n', 'point')
point1 = Point(3, 4)
print(point1, point1.lenght())
