def solution(w,h):
    
    answer = w * h
    a = gcd(w,h)
    b = h / w
    
    if b < 1:
        b = w / h
        swapd = w
        w = h
        h = swapd
    
    if w % a == 0:
        n = b * (w // a) * (w // a)
        
        for i in range(1, w//a):
            n -= int(b*i)
            n -= int(b*i)
        
        answer -= n * a
    else:
        n = b * (w // a) * (w // a)
        
        for i in range(1, w//a):
            n -= int(b*i)
            n -= int(b*i)
        
        answer -= n * a
        
        for i in range(1, w % (w // a) ):
            answer -= int(b*i)
            answer -= int(b*i)
    
    return answer 

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)