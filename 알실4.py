n = int(input())
a = [False, False] + [True] * (n-1)

result = []
for i in range(2, n+1):
    if a[i]:
        result.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
print(len(result))
