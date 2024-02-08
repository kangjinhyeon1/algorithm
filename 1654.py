n, m = map(int, input().split())
lan = []
for _ in range(n):
    lan.append(int(input()))


s = 1
d = max(lan)

while s <= d:
    cnt = (s + d) // 2
    a = 0
    for i in lan:
        a = a + (i // cnt)
    if a >= m:
        s = cnt + 1
    else:
        d = cnt - 1

print(d)
