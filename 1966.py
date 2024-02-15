# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     queue = list(map(int, input().split()))
#     cnt = 0

#     while True:
#         maximum = max(queue)
#         front = queue.pop(0)
#         unique = set(queue)
#         if cnt == m:
#             if cnt == 0:
#                 if len(unique) == 2:
#                     print(n - 1)
#                     break
#                 else:
#                     print(1)
#             else:
#                 print(cnt)
#             break
#         if maximum == front:
#             cnt = cnt + 1

#         else:
#             queue.append(front)

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    cnt = 0
    while queue:
        maximum = max(queue)
        front = queue.pop(0)
        m = m - 1

        if maximum == front:
            cnt = cnt + 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1
