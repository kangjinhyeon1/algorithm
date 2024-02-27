from collections import deque
import sys

t = int(sys.stdin.readline())

deque = deque()
for _ in range(t):
    cmd = sys.stdin.readline().split()
    match cmd[0]:
        case "push_front":
            deque.appendleft(int(cmd[1]))
        case "push_back":
            deque.append(int(cmd[1]))
        case "pop_front":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.popleft())
        case "pop_back":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.pop())
        case "size":
            print(len(deque))
        case "empty":
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        case "front":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[0])
        case "back":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[-1])
