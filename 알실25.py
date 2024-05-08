n, m = map(int, input().split())

video = list(map(int, input().split()))

start = 1
end = sum(video)
res = 0


while start <= end:
    cnt = 1
    tmp = 0
    mid = (start + end) // 2

    for i in video:
        if tmp + i <= mid:
            tmp = tmp + i
        else:
            cnt = cnt + 1
            tmp = i
    if cnt <= m:
        res = mid
        end = mid - 1
    else:
        start = mid + 1
print(res)
