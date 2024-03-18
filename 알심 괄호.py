n = int(input())

for _ in range(n):
    stack = []
    s = str(input())

    for i in s:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(i)
    if len(stack) > 0:
        print("NO")
    else:
        print("YES")
