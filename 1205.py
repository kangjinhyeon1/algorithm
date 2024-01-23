n, k, z = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))

    if n == z and score[-1] >= k:
        print(-1)
    else:
        for i in range(n):
            if score[i] <= k:
                print(i+1)
                break


n, k, z = map(int, input().split())

if n == 0:
    print(1)
else:
    score = list(map(int, input().split()))

    if n == z and score[-1] >= k:
        print(-1)
    else:
        result = n + 1
        for i in range(n):
            if score[i] <= k:
                result = i + 1
                break
        print(result)
