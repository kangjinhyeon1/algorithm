n = int(input())

Fac = 1
for i in range(n):
    Fac = Fac * (i + 1)

cnt = 0
for i in reversed(str(Fac)):
    if int(i) == 0:
        cnt = cnt + 1
    else:
        break

print(cnt)
