from heapq import heappush, heappop

def findMax(users, emoticons, emoidx, heap):
    if emoidx == len(emoticons):
        totalbuy = [0, 0] # 구독제 가입자 수, 구매 확정
        for rate, limit in users:
            userbuy = 0
            for price, salerate in emoticons:
                if salerate >= rate:
                    userbuy += price * (100 - salerate) // 100
                    
            if userbuy >= limit:
                totalbuy[0] += 1
            else:
                totalbuy[1] += userbuy
        heappush(heap, [-totalbuy[0], -totalbuy[1]])
    else:
        for salerate in [10,20,30,40]:
            emoticons[emoidx][1] = salerate
            findMax(users, emoticons, emoidx+1, heap)

def solution(users, emoticons):
    heap = []
    answer = []
    emoticons = [[price, 0] for price in emoticons]
    
    findMax(users, emoticons, 0, heap)
    
    answer = heappop(heap)
    
    return [-answer[0], -answer[1]]