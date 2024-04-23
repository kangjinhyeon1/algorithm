# 미로의 최단거리 통로

from collections import deque


graph = []

for i in range(7):
    s = list(map(int, input().split()))
    graph.append(s)


def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 7 or ny < 0 or ny >= 7:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx, ny))
            if graph[nx][ny] == 1:
                continue
    return graph[6][6]


print(bfs(0, 0))
