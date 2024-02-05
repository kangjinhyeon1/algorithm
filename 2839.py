n = int(input())

total = 0
while n >= 0:
    if n % 5 == 0:
        total = total + (n // 5)
        n = 0
        break
    else:
        n = n - 3
        total = total + 1
if n == 0:
    print(total)
else:
    print('-1')
