import sys

t = int(sys.stdin.readline())

n = []
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    n.append([x, y])

a = sorted(n, key=lambda x: (x[1], x[0]))

for i in a:
    print(f'{i[0]} {i[1]}')
