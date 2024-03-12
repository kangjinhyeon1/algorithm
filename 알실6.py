from collections import deque

n, m = map(int, input().split())

n = deque([i + 1 for i in range(n)])

for _ in range(len(n)-1):
    for i in range(m-1):
        a = n.popleft()
        n.append(a)
    n.popleft()

print(n)
