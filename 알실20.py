# 단지 번호 붙이기

from collections import deque


n = int(input())

graph = [[] * i for i in range(n)]

for i in range(n):
    s = str(input())
    for j in s:
        graph[i].append(int(j))

cnt = 0


def bfs(x, y):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    tmp = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                tmp = tmp + 1
                queue.append((nx, ny))
    cnt = cnt + 1
    return tmp


res = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            a = bfs(i, j)
            if a == 0:
                res.append(a+1)
            else:
                res.append(a)

print(cnt)
res.sort()
for i in res:
    print(i)
