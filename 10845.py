from collections import deque
import sys

n = int(sys.stdin.readline())

deque = deque()

for _ in range(n):
    cmd = sys.stdin.readline().split()
    match cmd[0]:
        case "push":
            deque.append(int(cmd[1]))
        case "front":
            if len(deque) > 0:
                print(deque[0])
            else:
                print(-1)
        case "back":
            if len(deque) > 0:
                print(deque[-1])
            else:
                print(-1)
        case "size":
            print(len(deque))
        case "empty":
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        case "pop":
            if len(deque) > 0:
                print(deque.popleft())
            else:
                print(-1)
