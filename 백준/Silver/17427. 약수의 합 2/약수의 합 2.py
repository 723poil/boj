input1 = int(input())

sum = 0

for i in range(1, input1 + 1):
    sum += (input1//i) * i
    
print(sum)