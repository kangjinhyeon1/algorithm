# 섬나라 아일랜드

from collections import deque


n = int(input())

graph = []

for i in range(n):
    s = list(map(int, input().split()))
    graph.append(s)

cnt = 0


def bfs(x, y):
    global cnt
    dx = [0, 0, 1, -1, 1, 1, -1, -1]
    dy = [1, -1, 0, 0, 1, -1, 1, -1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    cnt = cnt + 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

print(cnt)
