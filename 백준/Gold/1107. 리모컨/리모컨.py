N = int(input())
M = int(input())

isbreakdown = [False]*10

if M != 0:
    for i in list(map(int, input().split())):
        isbreakdown[i] = True

min_cnt = abs(N - 100)

for number in range(1000000):
    for i in range(len(str(number))):
        
        if isbreakdown[int(str(number)[i])] == True:
            break
        elif i == len(str(number))-1:
            min_cnt = min(min_cnt, abs(number-N)+ len(str(number)))

print(min_cnt)