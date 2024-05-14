# 역수열

n = int(input())

num = list(map(int, input().split()))
res = [0] * n

for i in range(n):
    for j in range(n):
        if num[i] == 0 and res[j] == 0:
            res[j] = i + 1
            break
        elif res[j] == 0:
            num[i] = num[i] - 1

for x in res:
    print(x, end=' ')
