a = int(input())
b = int(input())
c = int(input())

sum = str(a * b * c)

dic = {}
for key in sum:
    dic[key] = dic.get(key, 0) + 1

for i in range(10):
    if str(i) in dic:
        print(dic[str(i)])
    else:
        print(0)
