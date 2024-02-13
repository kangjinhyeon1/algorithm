# n = int(input())
# comparison = list(map(int, input().split()))

# a = int(input())
# value = list(map(int, input().split()))

# for i in value:
#     tmp = 0
#     for j in comparison:
#         if i == j:
#             tmp = 1
#             break
#     print(tmp)

n = int(input())
comparison = list(map(int, input().split()))

dic = {}
for key in comparison:
    dic[key] = dic.get(key, 0) + 1

a = int(input())
value = list(map(int, input().split()))

for i in value:
    j = dic.get(i)
    if j == None:
        print(0)
    else:
        print(1)
