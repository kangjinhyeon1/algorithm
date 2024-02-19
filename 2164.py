# n = int(input())

# card = []

# for i in range(n):
#     card.append(i + 1)

# while len(card) != 1:
#     card.pop(0)
#     card.append(card.pop(0))

# print(card[0])

from collections import deque

n = int(input())
deque = deque([i for i in range(1, n + 1)])

while len(deque) != 1:
    deque.popleft()
    deque.append(deque.popleft())

print(deque[0])
