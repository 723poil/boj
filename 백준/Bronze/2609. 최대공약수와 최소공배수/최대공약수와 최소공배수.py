a,b = map(int , input().split())

m = min(a, b)
ma = max(a, b)

for i in range(m, 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for i in range(ma, a*b + 1):
    if i % a == 0 and i % b == 0:
        print(i)
        break