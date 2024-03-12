s = list(str(input()))

stack = []
bar = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    elif s[i] == ")" and s[i-1] == "(":
        stack.pop()
        bar = bar + len(stack)
    elif s[i] == ")" and s[i-1] == ")":
        stack.pop()
        bar = bar + 1

print(bar)
