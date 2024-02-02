n = int(input())

for _ in range(n):
    m, s = map(str, input().split())
    result = []
    for i in s:
        for _ in range(int(m)):
            result.append(i)
    print("".join(result))
