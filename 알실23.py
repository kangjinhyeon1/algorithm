# 이분 검색
import sys
n, m = map(int, input().split())

num = list(map(int, sys.stdin.readline().split()))

num.sort()
start = 0
end = n - 1
while start <= end:
    mid = (start + end) // 2

    if num[mid] == m:
        print(mid+1)
        break
    elif num[mid] > m:
        end = mid - 1
    else:
        start = mid + 1
