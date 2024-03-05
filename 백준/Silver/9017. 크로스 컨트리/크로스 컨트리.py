import sys

input = sys.stdin.readline

def solution():
    T = int(input())
    
    result = []
    
    for _ in range(T):
        N = int(input())
        ranks = list(map(int, input().split()))
        
        teams_count = [0] * 201
        
        teams_sum = {}
        score = 1
        
        for team in ranks:
            teams_count[team] += 1
        
        for team in ranks:
            
            if teams_count[team] >= 6:
                if teams_count[team] == 6:
                    teams_sum[team] = [score, 0]
                elif teams_count[team] < 10:
                    teams_sum[team][0] += score
                elif teams_count[team] == 10:
                    teams_sum[team][1] = score
            
                score += 1
                teams_count[team] += 1
            
        rst = sorted(teams_sum.items(), key= lambda x: (x[1][0], x[1][1]))
                
        result.append(rst[0][0])
            
    return result
    
result = solution()

for rst in result:
    print(rst)  