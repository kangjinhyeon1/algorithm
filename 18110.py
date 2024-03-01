import sys


def round2(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


t = int(sys.stdin.readline())

n = []

if t:
    for _ in range(t):
        n.append(int(sys.stdin.readline()))

    n.sort()

    a = round2(t * 0.15)
    b = n[a:t-a]
    b = sum(b) / len(b)

    print(round2(b))
else:
    print(0)
