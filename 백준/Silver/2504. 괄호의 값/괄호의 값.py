
N = list(input())

i = 0
L = len(N)

cir = []
allsum = 0
before = 0

if len(N) % 2 > 0:
    before += 1

while i < L :
    if N[i] == '(' or N[i] == '[':
        cir.append(N[i])
    elif N[i] == ')':
        if len(cir)>0:
            k = 0
            for _ in range(len(cir)):
                x = cir.pop()
                if x=='[':
                    before += 1
                    break
                elif x == '(':
                    if k == 0:
                        cir.append(2)
                    else:
                        cir.append(2*k)
                    break
                else:
                    k += x
    elif N[i] == ']':
        if len(cir)>0:
            k = 0
            for _ in range(len(cir)):
                x = cir.pop()
                if x == '(':
                    before += 1
                    break
                elif x == '[':
                    if k == 0 :
                        cir.append(3)
                    else:
                        cir.append(3*k)
                    break
                else:
                    k += x
    i += 1

if before >0:
    print(0)

else:
    for j in cir:
        if j == '(' or j == '[':
            allsum = 0
            break
        allsum += j
    print(allsum)
