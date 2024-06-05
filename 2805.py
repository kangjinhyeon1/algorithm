n, m = map(int, input().split())

wood = list(map(int, input().split()))

start = 1
end = max(wood)

while start <= end:
    mid = (start + end) // 2
    a = 0
    for i in wood:
        if i - mid > 0:
            a = a + (i - mid)
    if a >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
