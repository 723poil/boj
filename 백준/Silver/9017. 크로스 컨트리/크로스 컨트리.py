import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():
    T = int(input())
    
    result = []
    
    for _ in range(T):
        N = int(input())
        ranks = list(map(int, input().split()))
        
        team = dict()
        
        checked = defaultdict(int)
        
        rank = 0
        while len(ranks) > 0:
            cur_team = ranks.pop(0)
            
            if checked[cur_team] == 0:
                checked[cur_team] = ranks.count(cur_team) + 1
                
            if checked[cur_team] == 6:
                rank += 1
                
                if team.get(cur_team) is None:
                    team[cur_team] = [[rank, 10000], rank]
                elif len(team[cur_team]) < 5:
                    team[cur_team].append(rank)
                    team[cur_team][0][0] += rank
                    
                elif len(team[cur_team]) == 5:
                    team[cur_team].append(rank)
                    team[cur_team][0][1] = rank
                    
        cur_rank = 10 ** 6
        cur_team = 0
        cur_last = 10 ** 6
        
        for key in team:
            sum_rank, last_team = team[key][0]
            
            if cur_rank > sum_rank or (cur_rank == sum_rank and cur_last > last_team):
                cur_rank = sum_rank
                cur_team = key
                cur_last = last_team
                
        result.append(cur_team)
            
    return result
    
result = solution()

for rst in result:
    print(rst)  