import math

n = int(input())
m = list(map(int, input().split()))

cnt = 0
tmp = 0

for i in m:
    if i > 3:
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                cnt = cnt + 1
                break
    else:
        if i == 1:
            cnt = 1
        else:
            tmp = tmp + 1
            cnt = 1
    if cnt == 0:
        tmp = tmp + 1
    cnt = 0
print(tmp)
