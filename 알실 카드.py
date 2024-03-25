from collections import deque

n = int(input())

queue = deque([i for i in range(1, n+1)])

while True:
    queue.popleft()
    if len(queue) == 1:
        print(queue.popleft())
        break
    queue.append(queue.popleft())
