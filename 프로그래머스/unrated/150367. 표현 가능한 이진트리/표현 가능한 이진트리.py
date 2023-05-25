from collections import deque
def solution(numbers):
#이진수를 저장할 빈 문자열을 생성합니다.
    answer = []
    
    def make_full_binary(binary):
        n = 1
        bn = len(binary)
        # 1 - 3 - 7 - 15 - 31 - 63
        while bn > n:
            n += (n+1)
        
        for _ in range(n - bn):
            binary = '0' + binary
        
        return binary           
    
#주어진 이진트리에 더미 노드를 추가하여 포화 이진트리로 만듭니다. 루트 노드는 그대로 유지합니다.
    for number in numbers:
        binary_number = bin(number).lstrip("0b")
        binary_number = make_full_binary(binary_number)
        
        root_idx = len(binary_number) // 2
        isBinary = True
        
        queue = deque()
        queue.append([0, root_idx, len(binary_number)-1])

        while queue and isBinary:
            start, mid, end = queue.pop()
            
            next_left_mid = (start+mid-1)//2
            next_right_mid = (mid+end+1)//2

            
            if (binary_number[next_left_mid] == '1' or binary_number[next_right_mid] == '1') and binary_number[mid] != '1':
                isBinary = False
                break
            else:
                if end - start > 2:
                    queue.appendleft([start, next_left_mid, mid-1])
                    queue.appendleft([mid+1, next_right_mid, end])
        if isBinary:
            answer.append(1)
        else:
            answer.append(0)
        
    return answer