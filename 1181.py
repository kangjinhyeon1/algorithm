n = int(input())

s = []
for i in range(n):
    s.append(input())

s = list(set(s))
s.sort()
s.sort(key=lambda x: len(x))

for i in s:
    print(i)
