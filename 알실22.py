# 토마토

from collections import deque
import sys

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
res = 0
queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))


def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))


bfs()

for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            sys.exit()
    res = max(res, max(i))

print(res - 1)
