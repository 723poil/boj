import math

def solution(s):
    answer = len(s)
    
    for i in range(1, len(s)):
        alist = []
        length = len(s)
        before_same = False
        before_string = ""
        
        for j in range(0, len(s), i):
            if j == 0:
                before_string = s[j:j+i]
                alist.append(1)
            elif before_string == s[j:j+i]:
                alist[-1] += 1
            else:
                before_string = s[j:j+i]
                alist.append(1)
        
        for cnt in alist:
            if cnt != 1:
                length = length - (i * (cnt-1)) + int(math.log(cnt, 10)) + 1
        
        answer = min(answer, length)
    
    return answer