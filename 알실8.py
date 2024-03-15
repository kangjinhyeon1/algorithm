formula = list(input())
stack = []
answer = ''

for tmp in formula:
    if tmp.isalpha():
        answer += tmp
    elif tmp == '(':
        stack.append(tmp)
    elif tmp == '*' or tmp == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(tmp)
    elif tmp == '+' or tmp == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(tmp)
    else:
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop()

while stack:
    answer += stack.pop()
print(answer)
