import sys

# 아직 해결 안됨 바둑이문제

m, t = map(int, input().split())

s = []
for _ in range(t):
    s.append(int(input()))


def dfs(i, max):
    if max > m:
        return
    if i == t:
        print(max)
    else:
        dfs(i+1, max+s[i])
        dfs(i+1, max)


print()
