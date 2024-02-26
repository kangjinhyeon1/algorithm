t = int(input())

rank = []
for _ in range(t):
    x, y = map(int, input().split())
    rank.append([x, y])

cnt = 1
for i in rank:
    for j in range(len(rank)):
        if i[0] != rank[j][0] and i[1] != rank[j][1]:
            if i[0] <= rank[j][0] and i[1] <= rank[j][1]:
                cnt = cnt + 1
    print(cnt)
    cnt = 1
