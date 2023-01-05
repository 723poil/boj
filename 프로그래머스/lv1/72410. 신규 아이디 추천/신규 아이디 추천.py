def solution(new_id):
    
    #1단계 - 대문자 -> 소문자
    answer = new_id.lower()
    new_id = answer
    
    #2단계 - 특정 문자 제거
    removestr = ''
    for x in new_id:
        if x.isdigit() or x.isalpha() or x in '-_.':
            continue
        else:
            answer = answer.replace(x, '')
    
    new_id = answer
    
    #3단계 - 연속된 . 을 하나의 .으로 치환
    while '..' in new_id:
        answer = new_id.replace('..', '.')
        new_id = answer
    
    #4단계 - 처음과 끝의 .을 제거
    answer = new_id.strip('.')
    new_id = answer
    
    #5단계 - 빈 문자열 -> 'a'
    if answer == '':
        answer = 'a'
        new_id = answer
    
    #6단계 - 16자 이상 -> 15자 제한
    if len(answer) > 15:
        answer = new_id[0:15]
        answer = answer.strip('.')
    
    #7단계 - 2자 이하일 경우 3자까지 확장
    if len(answer) < 3:
        if len(answer) == 1:
            answer = answer + answer[0] + answer[0]
        else:
            answer = answer + answer[1]
    
    return answer