n, m = map(int, input().split())
num = list(map(int, input().split()))

result = []
for i in range(n):
    for j in range(i+1, n):
        for x in range(j+1, n):
            num_sum = num[i] + num[j] + num[x]
            if num_sum <= m:
                result.append(num_sum)


print(max(result))
