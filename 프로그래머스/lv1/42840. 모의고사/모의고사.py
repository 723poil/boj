def solution(answers):
    answer = []
    
    # 1번 주기 - 12345
    # 2번 주기 - 21232425
    # 3번 주기 - 3311224455
    
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    
    len_1 = len(answer_1)
    len_2 = len(answer_2)
    len_3 = len(answer_3)
    
    score = [0,0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == answer_1[(i+1)%len_1 -1]:
            score[1] += 1
        if answers[i] == answer_2[(i+1)%len_2 -1]:
            score[2] += 1
        if answers[i] == answer_3[(i+1)%len_3 -1]:
            score[3] += 1
        
    max_score = max(score)
    
    for i in range(1, 4):
        if max_score == score[i]:
            answer.append(i)
    
    return answer