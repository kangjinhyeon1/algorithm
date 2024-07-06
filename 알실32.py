# 증가수열 만들기

n = int(input())

num = list(map(int, input().split()))
res = []
cnt = 1
current = 0
if num[0] > num[-1]:
    current = num[-1]
    num.pop()
    res.append("R")
else:
    current = num[0]
    num.pop(0)
    res.append("L")

while num:
    if num[0] < num[-1]:
        if current < num[0]:
            cnt = cnt + 1
            current = num[0]
            num.pop(0)
            res.append("L")
        elif current < num[-1]:
            cnt = cnt + 1
            current = num[-1]
            num.pop()
            res.append("R")
        else:
            break
    else:
        if current < num[-1]:
            cnt = cnt + 1
            current = num[-1]
            num.pop()
            res.append("R")
        elif current < num[0]:
            cnt = cnt + 1
            current = num[0]
            num.pop(0)
            res.append("L")
        else:
            break

print(cnt)
print(''.join(res))
