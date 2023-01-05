def solution(n):
    
    answer = ""
    con124 = ["4", "1", "2"]
    
    answer += con124[n%3]
    n = (n-1) // 3
    
    while n > 0:
        answer = con124[n%3] + answer
        n = (n-1) // 3
            
    
    return answer