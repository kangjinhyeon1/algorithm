a = int(input())
result = 0


def redivide(a):
    if (a == 1):
        print(0)
    if a % 2 == 0:
        n1 = a / 2
        n2 = a / 2
        result += n1 * n2
        redivide(n1)
        redivide(n2)
    else:
        n1 = int(a / 2)
        n2 = a - n1
        result += n1 * n2
        redivide(n1)
        redivide(n2)


redivide(a)

print(result)
