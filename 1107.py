# import sys


# n = int(input())
# t = int(input())
# no = list(map(int, input().split()))

# no.sort()

# if n == 100:
#     print(0)
#     sys.exit()

# cnt = 0
# m = 0
# for i in str(n):
#     m = int(i)
#     if int(i) not in no:
#         cnt = cnt + 1
#     else:
#         for j in range(10, 0, -1):
#             if j not in no and m - j >= 0:
#                 cnt = cnt + 1
#                 m = m - j
#                 print(m, j)
#                 break
#         for _ in range(m):
#             cnt = cnt + 1

# print(cnt)

import sys
input = sys.stdin.readline
target = int(input())
n = int(input())
broken = list(map(int, input().split()))

min_count = abs(100 - target)

for nums in range(1000001):
    nums = str(nums)

    for j in range(len(nums)):
        if int(nums[j]) in broken:
            break

        elif j == len(nums) - 1:
            min_count = min(min_count, abs(int(nums) - target) + len(nums))

print(min_count)
