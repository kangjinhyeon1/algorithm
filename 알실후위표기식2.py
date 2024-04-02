n = int(input())

s = str(input())

value = []
res = []

for _ in range(n):
    value.append(int(input()))

for i in s:
    if i == "*" or i == "/" or i == "+" or i == "-":
        if len(res) > 1:
            b, a = res.pop(), res.pop()
            match i:
                case "*":
                    res.append(a * b)
                case "/":
                    res.append(a / b)
                case "+":
                    res.append(a + b)
                case "-":
                    res.append(a-b)
    else:
        res.append(value[ord(i)-65])
print(f'{res[0]:.2f}')
