n = int(input())

holyday = []

for _ in range(n):
    a, b = map(int, input().split())
    holyday.append([a, b])

maximum = 0


def dfs(m, c):
    global maximum
    if m == n:
        if maximum < c:
            maximum = c
    else:
        if m <= n:
            dfs(m+holyday[m][0], c+holyday[m][1])
            dfs(m+1, c)


dfs(0, maximum)

print(maximum)
