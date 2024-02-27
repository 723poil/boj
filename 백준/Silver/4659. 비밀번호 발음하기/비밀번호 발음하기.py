import sys

input = sys.stdin.readline

# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
# 마지막 테스트 케이스는 end이며, 패스워드는 한글자 이상 20글자 이하의 문자열이다. 또한 패스워드는 대문자를 포함하지 않는다.

v_count = 0
m_count = 0

def find_m(t):
    m = ['a', 'e', 'i', 'o', 'u']
    
    if (m.count(t) > 0):
        return True;
    return False;

def find_e_o(t):
    eo = ['e', 'o']
    
    if (eo.count(t) > 0):
        return True;
    return False;

def validDoubleSpell(t, arr):
    if len(arr) == 0:
        return True
    
    if arr[-1] != t:
        return True
    
    if len(arr) == 1 and find_e_o(t):
        return True
    
    if len(arr) > 1 and find_e_o(t) and arr[-2] != t:
        return True
    
    return False

def count_valid(is_m):
    global v_count, m_count
    
    if (is_m and v_count < 0):
        v_count = 1
    elif (is_m):
        v_count += 1
    elif (not is_m and v_count > 0):
        v_count = -1
    else:
        v_count -= 1

def validate_password(p):
    global v_count, m_count
    tmp = []
    
    while len(p) > 0:
        t = p.pop()
        
        is_m = find_m(t)
        
        if (is_m):
            m_count = 1
            
        count_valid(is_m)
        
        if v_count == 3 or v_count == -3:
            return False
        
        if (validDoubleSpell(t, tmp)):
            tmp.append(t)
        else:
            return False
        
    if m_count != 1:
        return False
    
    return True
        

while True:
    m_count = 0
    v_count = 0
    
    password = input().rstrip('\n')
    result = True
    
    if (password == 'end'):
        break
    
    if (len(password) < 1 or len(password) > 20):
        result = False
        
    result = validate_password(list(password))
    
    if (result):
        text = '<' + password + '> is acceptable.'
        print(text)
    else:
        text = '<' + password + '> is not acceptable.'
        print(text)