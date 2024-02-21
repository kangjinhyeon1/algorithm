n, m = map(int, input().split())

GCD_N = n
GCD_M = m

while GCD_M:
    GCD_N, GCD_M = GCD_M, GCD_N % GCD_M

print(GCD_N)
print((n * m) // GCD_N)
