import sys

def upper_bound(start, end, search):
    if card[start] > search:
        return 0
    elif card[end-1] < search:
        return 0
    mid = (start+end)//2
    while start < end :
        if card[mid] <= search:
            start = mid+1
        else :
            end = mid
        mid = (start + end) // 2
    if card[end-1] == search:
        return end
    else:
        return 0

def lower_bound(start, end, search):
    if card[end] < search:
        return 0
    elif card[start] > search:
        return 0

    mid = (start + end) // 2
    while start < end:
        if card[mid] < search:
            start = mid+1
        else :
            end = mid
        mid = (start+end)//2
    if card[end] == search:
        return end
    else:
        return 0

if __name__ == '__main__' :
    N = int(sys.stdin.readline())
    card = list(map(int, sys.stdin.readline().split(' ')))
    M = int(sys.stdin.readline())
    card_search = list(map(int, sys.stdin.readline().split(' ')))
    card = sorted(card)

    for search in card_search:
        count = upper_bound(0, len(card), search) - lower_bound(0, len(card)-1, search)
        print(count, end= ' ')
