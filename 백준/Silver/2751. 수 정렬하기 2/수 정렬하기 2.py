N = int(input())

number = []

for _ in range(N):
    number.append(int(input()))

number.sort()

for i in range(N):
    print(number[i])