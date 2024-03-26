import heapq


t = int(input())

for _ in range(t):
    n = int(input())
    min_heap = []
    max_heap = []
    res = 0
    for _ in range(n):
        s, m = map(str, input().split())
        if s == "I":
            heapq.heappush(max_heap, int(m) * -1)
            heapq.heappush(min_heap, int(m))
        elif s == "D":
            if int(m) == -1 and len(min_heap) > 0:
                heapq.heappop(min_heap)
            elif int(m) == 1 and len(max_heap) > 0:
                heapq.heappop(max_heap)
    for i in max_heap:
        if (i * -1) not in min_heap:
            res.append(i * -1)
