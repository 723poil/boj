from collections import deque

lazer = str(input())

bar_left = 0
lazer_number = 0
sum = 0

for i in range(len(lazer)):
    if lazer[i] == '(' and lazer[i+1] == ')' and i< len(lazer)-1:
        if bar_left == 0:
            continue
        else:
            lazer_number += 1
    elif lazer[i] == '(':
        if lazer_number != 0:
            sum += bar_left * lazer_number
            lazer_number = 0
        bar_left += 1
    elif lazer[i] == ')' and lazer[i-1] != '(':
        sum += bar_left * lazer_number + 1
        bar_left -= 1
        lazer_number = 0

print(sum)