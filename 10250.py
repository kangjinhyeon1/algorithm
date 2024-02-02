# t = int(input())

# for i in range(t):
#     h, w, n = map(int, input().split())
#     a = n // h + 1
#     floor = n % h
#     print(floor * 100 + a)

t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    a = n // h
    floor = n % h
    if floor == 0:
        print((h * 100) + a)
    else:
        print((floor * 100) + (a + 1))
