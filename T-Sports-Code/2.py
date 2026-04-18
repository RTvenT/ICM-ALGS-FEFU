from math import comb


n = int(input())

print(comb(n**2, 2) - 4 * (n - 1) * (n - 2))