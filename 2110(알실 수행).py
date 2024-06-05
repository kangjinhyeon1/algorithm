n, c = map(int, input().split())

num = []
for _ in range(n):
    num.append(int(input()))
num.sort()

start = 1
end = num[-1] - num[0]
res = 0

while (start <= end):
    mid = (start + end) // 2
    current = num[0]
    cnt = 1

    for i in range(1, n):
        if num[i] >= current + mid:
            cnt += 1
            current = num[i]

    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1

print(res)
