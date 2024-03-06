import sys
import math

input = sys.stdin.readline

def solution():
    N = int(input())
    roads = list(map(int, input().split()))
    oils = (list(map(int, input().split())))[:-1]
    
    sales = 0
    cur_oil = 1000000001
    
    for i in range(N-1):
        cur_oil = min(cur_oil, oils[i])
        sales += (roads[i] * cur_oil)
                
    return sales
    
print(solution())