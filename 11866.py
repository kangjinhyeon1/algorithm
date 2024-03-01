from collections import deque
import sys
n, k = map(int, input().split())

yo = []
result = []
for i in range(1, n + 1):
    yo.append(i)

b = k - 1
while len(yo) != 1:
    result.append(str(yo.pop(b)))
    b = (b + (k-1)) % len(yo)
result.append(str(yo[0]))

print('<' + ', '.join(result) + '>')


# 입력 받기
n, k = map(int, input().split())

# 양방향 연결 리스트(deque) 생성
deq = deque([i for i in range(1, n+1)])

# 요세푸스 순열 생성
res = []
while len(deq) != 0:
    for _ in range(k-1):
        # k-1번째 노드까지 deq 맨 뒤로 이동
        deq.append(deq.popleft())
    # k번째 노드 삭제 후 결과 배열에 추가
    res.append(str(deq.popleft()))

# 결과 출력
print('<'+', '.join(res)+'>')
