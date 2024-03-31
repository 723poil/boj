from sys import stdin

input = stdin.readline

def find_case(coins: list, k: int):
    
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for coin in coins:
        for d in range(coin, k+1):
            dp[d] += dp[d - coin]
            
    return dp[-1]
    

def solution():
    n, k = map(int, input().split())
    
    coins = []
    
    for _ in range(n):
        coin = int(input())
        
        if coin <= k:
            coins.append(coin)
            
    coins.sort(key= lambda x: -x)
    
    return find_case(coins, k)
    

print(solution())