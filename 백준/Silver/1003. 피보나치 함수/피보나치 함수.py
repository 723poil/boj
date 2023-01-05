n = input()

zerocount = [1, 0 ,1]
onecount = [0, 1, 1]

for i in range(int(n)):
    a = int(input())

    while len(zerocount)-1 < a:
        zerocount.append(int(zerocount[len(zerocount)-1])+int(zerocount[len(zerocount)-2]))
        onecount.append(int(onecount[len(onecount)-1])+int(onecount[len(onecount)-2]))

    print(str(zerocount[int(a)])+" "+str(onecount[int(a)]))