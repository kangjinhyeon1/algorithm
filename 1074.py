n, r, c = map(int, input().split())

# 분할 정복 풀이
# res = 0

# while n != 0:
#     n = n - 1

#     if r < 2 ** n and c < 2 ** n:
#         res = res + ((2 ** n) * (2 ** n) * 0)
#     elif r < 2 ** n and c >= 2 ** 2:
#         res = res + ((2 ** n) * (2 ** n) * 1)
#         c = c - (2 ** n)
#     elif r >= 2 ** n and c < 2 ** n:
#         res = res + ((2 ** n) * (2 ** n) * 2)
#         r = r - (2 ** n)
#     else:
#         res = res + ((2 ** n) * (2 ** n) * 3)
#         r = r - (2 ** n)
#         c = c - (2 ** n)

# print(res)

# 재귀 풀이

# def solution(n, r, c):
#     if n == 0:
#         return 0
#     return 2 * (r % 2) + (c % 2) + 4 * solution(n - 1, int(r/2), int(c/2))


# print(solution(n, r, c))
