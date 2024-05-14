# 씨름 선수

n = int(input())

si = []

for _ in range(n):
    si.append(list(map(int, input().split())))

si.sort(key=lambda x: (-x[0]))

h = si[0][0]
w = si[0][1]
cnt = 1

for i in range(1, n):
    if si[i][1] > w:
        cnt = cnt + 1
        w = si[i][1]

print(cnt)
