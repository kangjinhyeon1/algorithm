n = int(input())

visited = [0 * i for i in range(0, n+1)]


def dfs(a):
    if a == n+1:
        li = []
        for i in range(len(visited)):
            if visited[i] == 1:
                li.append(i)
        print(li)
    else:
        visited[a] = 1
        dfs(a+1)
        visited[a] = 0
        dfs(a+1)


dfs(1)

print()
