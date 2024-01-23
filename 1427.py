n = input()
result = []
for i in n:
    result.append(i)
result.sort(reverse=True)
result = ''.join(result)
print(result)
