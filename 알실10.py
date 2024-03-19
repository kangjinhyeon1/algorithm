import sys


n = int(input())

m = list(map(int, input().split()))

# visited = [0 * i for i in range(0, n+1)]


# def dfs(a, s):
#     if a == n+1:
#         if s == sum(m) // 2:
#             print("YES")
#             sys.exit()
#     else:
#         visited[a] = 1
#         dfs(a+1, s+m[a])
#         visited[a] = 0
#         dfs(a+1, s)


# dfs(0, 0)

def DFS(i, s):
    if s > sum(m):
        return
    if i == n:
        if s == (sum(m)-s):
            print("YES")
            sys.exit(0)
    else:
        DFS(i+1, s+m[i])
        DFS(i+1, s)


DFS(0, 0)

print("NO")

print()
