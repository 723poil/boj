key_coord = {
    1 : [0,0], 2 : [0,1], 3 : [0,2],
    4 : [1,0], 5 : [1,1], 6 : [1,2],
    7 : [2,0], 8 : [2,1], 9 : [2,2],
               0 : [3,1]
}

def solution(numbers, hand):
    answer = ''
    
    Lcur = [3, 0]
    Rcur = [3, 2]
    
    for i in numbers:
        if i in [1,4,7]: #왼손 사용
            answer = answer + 'L'
            Lcur = key_coord[i]
        elif i in [3,6,9]: #오른손 사용
            answer = answer + 'R'
            Rcur = key_coord[i]
        else: #중간 번호
            #좌표상 위치
            number = key_coord[i]
            
            # 유클리드 거리 x -> 맨해튼 거리 O
            #왼손과의 거리
            Ldis = abs(number[0] - Lcur[0]) + abs((number[1] - Lcur[1])) 
            #오른손과의 거리
            Rdis = abs(number[0] - Rcur[0]) + abs(number[1] - Rcur[1])
            
            if Ldis < Rdis: # 왼손이 더 가까울 경우
                answer = answer + 'L'
                Lcur = number
            elif Ldis > Rdis: # 오른손이 더 가까울 경우
                answer = answer + 'R'
                Rcur = number
            else: # 거리가 같을 경우
                if hand == 'right':
                    answer = answer + 'R'
                    Rcur = number
                else:
                    answer = answer + 'L'
                    Lcur = number
            
    return answer