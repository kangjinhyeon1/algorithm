# 중복순열 구하기
n, m = map(int, input().split())

graph = [0] * m
cnt = 0


def dfs(i):
    global cnt
    if i == m:
        for k in graph:
            print(k, end=' ')
        print()
        cnt = cnt + 1
        return
    else:
        for k in range(1, n+1):
            graph[i] = k
            dfs(i + 1)


dfs(0)
print(cnt)
