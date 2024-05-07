n = int(input())
m = int(input())

graph = [[] * i for i in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)

print(graph)
