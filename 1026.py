# x = int(input())

# y = list(map(int, input().split()))
# z = list(map(int, input().split()))

# y.sort()
# z.sort(reverse=True)

# result = 0
# for i in range(x):
#     result = result + (y[i] * z[i])

# print(result)

x = int(input())

y = list(map(int, input().split()))
z = list(map(int, input().split()))

result = 0
for i in range(x):
    result += min(y) * max(z)
    y.pop(y.index(min(y)))
    z.pop(z.index(max(z)))

print(result)
