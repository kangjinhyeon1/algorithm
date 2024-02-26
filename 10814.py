t = int(input())

age = []
for _ in range(t):
    k, n = map(str, input().split())
    age.append([int(k), n])

n = sorted(age, key=lambda x: x[0])

for i in n:
    print(f'{i[0]} {i[1]}')
