A,B,V = map(int, input().split())

a = (V-A) // (A-B) + 1

if (V-A) % (A-B) != 0:
    a += 1

print(a)