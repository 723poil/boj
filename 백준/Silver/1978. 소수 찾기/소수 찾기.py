def find(a):
    for i in range(2, int(a/2)+ 1):
        if a % i == 0:
            return 0
    
    return 1

N = int(input())

number = list(map(int, input().split()))

sum = 0
for i in number:
    if i == 1:
        continue
    elif i // 2 < 2: 
        sum += 1
        continue
    sum += find(i)

print(sum)