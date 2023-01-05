N = int(input())

count = 0
i = 0

while True:
    i += 1
    temp = 0
    apocalypse = str(i)
    if apocalypse.count('666') >= 1:
        count += 1
        temp = i
    if count == N:
        print(temp)
        break