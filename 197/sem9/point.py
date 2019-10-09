from complex import Complex


class Point(Complex):
    def length(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __str__(self):
        return "({},{})".format(self.re, self.im)


point = Point(3, 4)

print(point, point.length())
print(Point(3, 5) + Point(-1, 9))
