t = int(input())

for _ in range(t):
    num = int(input())
    d = [1, 2, 3] + [0] * (num + 1)
    if num == 1:
        print(1)
    elif num == 2:
        print(2)
    elif num == 3:
        print(4)
    else:
        for i in range(4, num+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        print(d[num])
