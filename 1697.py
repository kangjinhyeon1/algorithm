from collections import deque


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(graph[x])
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= m and not graph[nx]:
                graph[nx] = graph[x] + 1
                q.append(nx)


m = 10 ** 5
graph = [0] * (m + 1)
n, k = map(int, input().split())

bfs()
