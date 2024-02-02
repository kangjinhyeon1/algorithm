import sys

n, m, b = map(int, input().split())

li = []
for _ in range(n):
    # li.append(list(map(int, input().split())))
    li.append([int(x) for x in sys.stdin.readline().rstrip().split()])

level = 0
tmp = int(1e9)

for i in range(257):
    max = 0
    min = 0
    for x in range(n):
        for y in range(m):
            if li[x][y] > i:
                max += li[x][y] - i
            else:
                min += i - li[x][y]
    if min > max + b:
        continue
    count = max * 2 + min

    if count <= tmp:
        tmp = count
        level = i

print(tmp, level)
