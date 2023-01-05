import sys
INF = int(1e9)

input = sys.stdin.readline

N = int(input())

maxdp = list(map(int, input().split()))
mindp = maxdp.copy()
maxtemp = [0, 0, 0]
mintemp = [INF, INF, INF]

for i in range(N-1):
    num = str(input())
    for ind, val in enumerate(num):
        if ind % 2 != 0:
            continue
        ind = ind // 2
        for j in range(3):
            if abs(j-ind) <= 1 and maxtemp[ind] < maxdp[j]+int(val):
                maxtemp[ind] = maxdp[j]+int(val)
            if abs(j-ind) <= 1 and mintemp[ind] > mindp[j]+int(val):
                mintemp[ind] = mindp[j]+int(val)
    for j in range(3):
        maxdp[j] = maxtemp[j]
        mindp[j] = mintemp[j]
        maxtemp[j] = 0
        mintemp[j] = INF

print(max(maxdp), min(mindp))