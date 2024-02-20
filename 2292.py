# n = int(input())

# if n == 1:
#     print(1)
# else:
#     cnt = 1
#     tmp = 1
#     while True:
#         tmp = tmp + (cnt * 6)
#         if n < tmp:
#             print(cnt + 1)
#             break
#         else:
#             cnt = cnt + 1

n = int(input())

num = 1
cnt = 1

while n > num:
    num = num + (cnt*6)
    cnt = cnt + 1

print(cnt)
