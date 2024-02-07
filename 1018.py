n, m = map(int, input().split())
b = []
result = []

for _ in range(n):
    b.append(input())

for i in range(n-7):
    for j in range(m-7):
        d1 = 0
        d2 = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if b[x][y] != 'B':
                        d1 = d1 + 1
                    if b[x][y] != 'W':
                        d2 = d2 + 1
                else:
                    if b[x][y] != 'W':
                        d1 = d1 + 1
                    if b[x][y] != 'B':
                        d2 = d2 + 1
        result.append(d1)
        result.append(d2)

print(min(result))
