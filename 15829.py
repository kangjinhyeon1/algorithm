n = int(input())
s = str(input())

sum = 0
for i in range(len(s)):
    sum = sum + (ord(s[i]) - 96) * (31 ** i)

print(sum % 1234567891)
