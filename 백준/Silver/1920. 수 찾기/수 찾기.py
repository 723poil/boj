def find(number, a, s, e):
    mid = (s + e) // 2 

    if number[mid] == a:
        return 1
    elif mid == 0 or mid == e:
        return 0
    elif number[mid] > a:
        return find(number, a, s, mid)
    elif number[mid] < a:
        if mid == (mid + e) // 2 :
            return find(number, a, e, e)
        return find(number, a, mid, e)

N = int(input())

number = list(map(int, input().split()))
number.sort()

M = int(input())

findN = list(map(int, input().split()))

for i in range(M):
    print(find(number, findN[i], 0, len(number)-1))