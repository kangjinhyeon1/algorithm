# def fibo(n):
#     global zero
#     global one
#     if n == 0:
#         zero = zero + 1
#         return 0
#     elif n == 1:
#         one = one + 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)


# n = int(input())
# zero = 0
# one = 0

# a = []
# for i in range(n):
#     a.append(int(input()))

# for i in a:
#     fibo(i)
#     print(f'{zero} {one}')
#     zero = 0
#     one = 0

zero = [1, 0, 1]
one = [0, 1, 1]


def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f'{zero[num]} {one[num]}')


n = int(input())

for _ in range(n):
    fibo(int(input()))
