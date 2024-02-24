while True:
    n = list(map(int, input().split()))
    n.sort()
    if n[0] == 0 and n[1] == 0 and n[2] == 0:
        break
    if pow(n[0], 2) + pow(n[1], 2) == pow(n[2], 2):
        print("right")
    else:
        print("wrong")
