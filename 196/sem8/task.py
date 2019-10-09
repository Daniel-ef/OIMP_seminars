
def gen_range(max_digit, cnt_digits):
    if cnt_digits > 0:
        for cur_digit in range(max_digit + 1):
            for tail in gen_range(cur_digit - 1, cnt_digits - 1):
                yield cur_digit * 10 ** (cnt_digits - 1) + tail
    else:
        yield 0


print(sum(gen_range(4, 3)))

print(max(gen_range(4, 3)))
print(max(*gen_range(4, 3)))
