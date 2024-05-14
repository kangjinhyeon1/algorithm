# 회의실 배정

n = int(input())

room = []

for _ in range(n):
    room.append(list(map(int, input().split())))

room.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end = 0

for a, b in room:
    if end <= a:
        cnt = cnt + 1
        end = b

print(cnt)
