t = int(input())

for _ in range(t):
    n, s, e, k = map(int, input().split())

    num = list(map(int, input().split()))
    num = num[s-1:e]
    num.sort()
    print(num[k-1])
