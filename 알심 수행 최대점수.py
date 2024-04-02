n, m = map(int, input().split())

a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append([x, y])

maximum = 0


def dfs(i, t, z):
    global maximum
    if i == n:
        if t >= 0:
            if maximum < z:
                maximum = z
    else:
        dfs(i+1, t-a[i][1], z + a[i][0])
        dfs(i+1, t, z)


dfs(0, m, maximum)

print(maximum)
