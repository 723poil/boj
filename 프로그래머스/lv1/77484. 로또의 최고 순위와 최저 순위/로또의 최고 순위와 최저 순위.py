def solution(lottos, win_nums):
    
    zero_n = lottos.count(0)
    win_count = 0
    
    for win_num in win_nums:
        if win_num in lottos:
            win_count += 1
            
    rank = {
        6:1,
        5:2,
        4:3,
        3:4,
        2:5,
        1:6,
        0:6
    }
        
    return [rank[win_count+zero_n], rank[win_count]]