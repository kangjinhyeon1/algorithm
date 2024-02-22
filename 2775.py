n = int(input())

for _ in range(n):
    k = int(input())
    m = int(input())

    base = [x for x in range(1, m + 1)]

    for i in range(k):
        for j in range(1, m):
            base[j] = base[j] + base[j - 1]
    print(base[-1])
