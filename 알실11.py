import sys

m, t = map(int, input().split())

s = []
for _ in range(t):
    s.append(int(input()))

res = []


def DFS(i, max):
    if max > m:
        return
    if i == t:
        res.append(max)
    else:
        DFS(i+1, max+s[i])
        DFS(i+1, max)


DFS(0, 0)
print(max(res))
