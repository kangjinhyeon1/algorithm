# 동전 교환
n = int(input())

coin = list(map(int, input().split()))

coin.sort(reverse=True)

s = int(input())
cnt = 0

for i in coin:
    if s % i > 0:
        cnt = cnt + s // i
        s = s % i
    else:
        cnt = cnt + int(s/i)
        break

print(cnt)
