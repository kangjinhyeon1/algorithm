n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in m:
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
