# 시간초과
# from collections import deque

# n = int(input())

# queue = deque([])
# stack = []

# for _ in range(n):
#     queue.append(int(input()))

# while len(queue) > 1:
#     queue = deque(sorted(queue))
#     a, b = queue.popleft(), queue.popleft()
#     queue.append(a+b)
#     stack.append(a+b)

# print(sum(stack))

# 우선순위 큐 사용(시간초과 해결)

import heapq

n = int(input())
card = []
total = 0

for _ in range(n):
    heapq.heappush(card, int(input()))

while len(card) > 1:
    a, b = heapq.heappop(card), heapq.heappop(card)
    c = a + b

    heapq.heappush(card, c)
    total = total + c

print(total)
