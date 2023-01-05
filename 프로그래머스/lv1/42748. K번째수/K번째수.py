def solution(array, commands):
    answer = []
    
    for command in commands:
        before_answer = array[command[0]-1: command[1]]
        before_answer = sorted(before_answer)
        answer.append(before_answer[command[2]-1])
            
    return answer