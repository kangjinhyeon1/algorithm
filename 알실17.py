# 송아지 찾기

from collections import deque
import sys

n, m = map(int, input().split())

d = [0] * 10001
queue = deque()
queue.append(n)
d[n] = 1
cnt = 0

while (queue):
    length = len(queue)
    for _ in range(length):
        a = queue.popleft()
        for i in [a-1, a+1, a+5]:
            if i == m:
                print(cnt+1)
                sys.exit()
            if i > 0 and i <= 10000 and d[i] == 0:
                d[i] = 1
                queue.append(i)
    cnt += 1
