# 랜선자르기
n, m = map(int, input().split())
lan = []
for _ in range(n):
    lan.append(int(input()))


start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    a = 0
    for i in lan:
        a = a + (i // mid)
    if a >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
