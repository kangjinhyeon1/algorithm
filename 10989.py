import sys

t = int(sys.stdin.readline())

n = [0] * (10000 + 1)

for _ in range(t):
    a = int(sys.stdin.readline())
    n[a] = n[a] + 1

for i in range(len(n)):
    if n[i] != 0:
        for _ in range(n[i]):
            print(i)
