q = int(input())

count = 1
a = 1
r = 6

while a < q:
    count += 1
    a += r
    r += 6

print(str(count)) 