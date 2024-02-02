s = input().lower()

dic = {}
for key in s:
    dic[key] = dic.get(key, 0) + 1
d2 = sorted(dic.items(), key=lambda x: x[1], reverse=True)

if len(d2) > 1 and d2[0][1] == d2[1][1]:
    print("?")
else:
    print(d2[0][0].upper())
