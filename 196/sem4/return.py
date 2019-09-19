# len = len("abba")

len("abba")

#  sum = a + b  dont do it


def sum_diff(a: int, b: int) -> (int, int):
    if a > 10:
        return a, b
    return a + b, a - b


sum_a, diff_a = sum_diff(5, 4)
print(sum_a, diff_a)
