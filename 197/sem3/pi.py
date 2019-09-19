import math

n = int(input())
pi_eps = 4 * sum([(-1)**i / (2 * i + 1) for i in range(n)])
print(pi_eps, math.pi)
