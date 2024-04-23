# 사과나무(미해결)

from collections import deque
n = int(input())

graph = []
for i in range(n):
    s = list(map(int, input().split()))
    graph.append(s)

res = []
res.append(graph[n//2][n//2])
graph[n//2][n//2] = 0


def bfs(z):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((z, z))
    for _ in range(z):
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                res.append(graph[nx][ny])
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


bfs(n//2)

print(sum(res))
