import sys

input = sys.stdin.readline

N = int(input())

meeting = []

for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting.sort(key=lambda user: (user[0], user[1]))

before = meeting[0]
count = 1

i = 1
while i < N:
    after = meeting[i]

    if after[1] < before[1] and after[0] != before[0]:      # 회의 간격이 더 적고 빨리 끝나는 회의인 경우 ( 시작시간은 다를때 )
        before = meeting[i]
        i += 1
        continue

    if after[0] == after[1]:      # 시작 시간과 끝 시간이 같을 경우
        before = meeting[i]
        count += 1
        i += 1
        continue

    if after[0] == before[0] and before[0] != before[1]:     # 시작 시간이 같을 경우 (최소만 따지기 때문)
        i += 1
        continue
    
    if after[0] >= before[1]:
        before = meeting[i]
        i += 1
        count += 1
    else:
        i += 1
        
print(count)