import math

N = list(map(int, input().split()))

sum = 0

for i in range(len(N)):
    sum += int(pow(N[i], 2))

mod = sum % 10

print(mod)