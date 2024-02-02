n = list(map(int, input().split()))

s = sorted(n)
if n == s:
    print("ascending")
else:
    s.sort(reverse=True)
    if n == s:
        print("descending")
    else:
        print("mixed")
