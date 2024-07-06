# 마구간 정하기

n, c = map(int, input().split())

horse = []

for _ in range(n):
    horse.append(int(input()))
horse.sort()

start = 1
end = horse[-1] - horse[0]
res = 0

while (start <= end):
    mid = (start + end) // 2
    current = horse[0]
    cnt = 1

    for i in range(1, n):
        if horse[i] >= current + mid:
            cnt += 1
            current = horse[i]

    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
