while True:
    msg = str(input())
    stack = []
    if msg == ".":
        break
    elif msg[-1] != ".":
        print("no")
    else:
        for i in msg:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
                    break
            elif i == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(i)
                    break
        if len(stack) == 0:
            print('yes')
        else:
            print('no')
