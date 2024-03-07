import sys
sys.setrecursionlimit(10000)

t = int(input())


def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0 <= nx < m) and (0 <= ny < n):
            if field[ny][nx] == 1:
                field[ny][nx] = 0
                dfs(nx, ny)


for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1
    cnt = 0
    for i in range(m):
        for j in range(n):
            if field[j][i] == 1:
                dfs(i, j)
                cnt = cnt + 1
    print(cnt)
