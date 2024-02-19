n = int(input())

for i in range(1, n + 1):
    num = sum(map(int, str(i)))
    add = i + num

    if n == add:
        print(i)
        break
    if i == n:
        print(0)
