# t = int(input())

# n = []
# for _ in range(t):
#     n.append(int(input()))

# print(round(sum(n) / len(n)))

# sort = sorted(n)
# print(sort[t // 2])


# if len(n) > 1:
#     dic = {}
#     for key in n:
#         dic[key] = dic.get(key, 0) + 1
#     if list(dic.keys())[0] < 0:
#         if list(dic.values())[0] == list(dic.values())[1]:
#             dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
#             print(dic[1][0])
#         else:
#             dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
#             print(dic[0][0])
#     else:
#         if list(dic.values())[0] == list(dic.values())[1]:
#             print(list(dic.keys())[1])
#         else:
#             print(list(dic.keys())[0])
# else:
#     print(n[0])

# n.sort()

# print(n[-1] - n[0])

t = int(input())

n = []
count = {}
for _ in range(t):
    n.append(int(input()))

for key in n:
    count[key] = count.get(key, 0) + 1

print(round(sum(n) / len(n)))

sort = sorted(n)
print(sort[t // 2])


freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

n.sort()

print(n[-1] - n[0])
