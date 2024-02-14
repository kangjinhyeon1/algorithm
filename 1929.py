# import math

# n, m = map(int, input().split())

# cnt = 0
# for i in range(n, m+1):
#     for j in range(2, int(math.sqrt(i) + 1)):
#         if i % j == 0:
#             cnt = 1
#             break
#     if i == 1:
#         cnt = 1
#     if cnt == 0:
#         print(i)
#     cnt = 0

def is_prime_num(n):
    arr = [True] * (n + 1)  # 특정 수가 지워졌는지 아닌지 확인하기 위한 배열
    arr[0] = False
    arr[1] = False

    for i in range(2, n + 1):
        if arr[i] == True:  # 특정 수가 지워지지 않았다면 (소수여서)
            j = 2

            while (i * j) <= n:
                arr[i*j] = False  # i의 배수의 값을 False로 지워준다.
                j += 1

    return arr


arr = is_prime_num(50)  # 0 ~ 50중 소수를 구하기 위한 함수

for i in range(len(arr)):
    if arr[i] == True:
        print(i, end=' ')
