n = list(str(input()))

numberstack = []
operation = []

sum = 0
while len(n) > 0:
    a = n.pop(0)

    if a == '-' or a == '+':
        numberstack.append(sum)
        operation.append(a)
        sum = 0
    else:
        sum = sum * 10 + int(a)        

numberstack.append(sum)
ssum = numberstack.pop(0)

i = 0
besum = 0
isminus = False
while i < len(numberstack):

    if isminus == False:
        if operation[i] == '-':
            isminus = True
            besum += numberstack[i]
        else:
            ssum += numberstack[i]
    else:
        if operation[i] == '+':
            besum += numberstack[i]
        else:
            ssum -= besum
            besum = numberstack[i]

    i += 1

ssum -= besum

print(ssum)