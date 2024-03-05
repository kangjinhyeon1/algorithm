t = int(input())

n = list(map(int, input().split()))


def round2(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


result = round2(sum(n)/t)
print(result)

tmp = abs(n[0] - result)
res = []
for i in n:
    if abs(i - result) <= tmp:
        res.append(i)
        tmp = abs(i-result)

if result in n:
    print(n.index(result)+1)
else:
    for i in res:
        if max(res) <= i:
            print(n.index(i)+1)
            break
