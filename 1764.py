n, m = map(int, input().split())

dic2 = {}
li = []
for _ in range(n + m):
    li.append(str(input()))

li2 = li[n+2:]
for key in li2:
    dic2[key] = dic2.get(key, 0) + 1

result = []
print(dic2)
# for i in li:
#     if dic2[i] == None:
#         print(dic2[i])
# if dic2[i] != None:
#     result.append(i[0])
# else:
#     a = 0
# print(len(result))
# for i in result:
#     print(i)
