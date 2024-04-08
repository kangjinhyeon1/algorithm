num = [int(input()) for _ in range(9)]
numSum = sum(num)
for faker1 in range(8):
    for faker2 in range(faker1 + 1, 9):
        if numSum - num[faker1] - num[faker2] == 100:
            f1, f2 = num[faker1], num[faker2]
            num.remove(f1)
            num.remove(f2)
            for t in sorted(num):
                print(t)
            break
    if len(num) == 7:
        break
