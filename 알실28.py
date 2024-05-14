# 창고 정리

n = int(input())

box = list(map(int, input().split()))
m = int(input())

box.sort()

while m > 0:
    a = int(box.index(max(box)))
    b = int(box.index(min(box)))
    box[a] = box[a] - 1
    box[b] = box[b] + 1
    m = m - 1

print(max(box) - min(box))
