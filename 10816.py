t = int(input())

card = list(map(int, input().split()))

dic = {}
for key in card:
    dic[key] = dic.get(key, 0) + 1
n = int(input())

keys = list(map(int, input().split()))

for i in keys:
    j = dic.get(i)
    if j == None:
        print(0)
    else:
        print(j)
