n = int(input())

tmp = 1
stack = []
result = []
flag = False
for _ in range(n):
    end = int(input())
    while tmp <= end:
        stack.append(tmp)
        result.append("+")
        tmp += 1

    if stack[-1] == end:
        stack.pop()
        result.append("-")

    else:
        flag = True
        break

if flag == True:
    print("NO")
else:
    for i in result:
        print(i)
