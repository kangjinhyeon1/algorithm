n, m = map(int, input().split())
n = list(map(int, str(n)))

res = []
for i in range(len(n)):
    while m != 0 and len(res) != 0 and res[-1] < n[i]:
        res.pop()
        m = m - 1
    res.append(n[i])

if m != 0:
    print(res[:len(res)-m])
else:
    print(res)
