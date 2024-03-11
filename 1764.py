import sys

n, m = map(int, sys.stdin.readline().split())
a = []
b = []
for _ in range(n):
    a.append(str(sys.stdin.readline().rstrip()))

for _ in range(m):
    b.append(str(sys.stdin.readline().rstrip()))

result = list(set(a) & set(b))
result.sort()

print(len(result))

for i in result:
    print(i)
