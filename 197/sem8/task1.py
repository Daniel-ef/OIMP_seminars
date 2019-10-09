def gen_numbers(max_digit, digit_num):
    if digit_num > 0:
        for i in range(max_digit + 1):
            for tail in gen_numbers(i - 1, digit_num - 1):
                yield i * 10 ** (digit_num - 1) + tail
    else:
        yield 0


# 210 310 320 321 410 420 421 430 431 432
print(*gen_numbers(4, 3))

