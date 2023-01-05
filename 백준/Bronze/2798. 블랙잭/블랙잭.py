N, M = map(int, input().split())

inputdata = list(map(int, input().split()))
blackjack = []

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = inputdata[i] + inputdata[j] + inputdata[k]
            if  sum <= M:
                if len(blackjack) == 0:
                    blackjack.append(sum)
                elif sum > blackjack[0]:
                    blackjack.clear()
                    blackjack.append(sum)

print(str(blackjack[0]))