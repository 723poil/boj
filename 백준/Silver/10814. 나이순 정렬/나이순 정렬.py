N = int(input())

order_age = []

for i in range(N):
    a, n = map(str, input().split())
    
    order_age.append((int(a), n))

order_age.sort(key= lambda user:(user[0]))

for i in order_age:
    print(i[0], i[1])