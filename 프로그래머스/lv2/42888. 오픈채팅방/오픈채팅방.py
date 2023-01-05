def solution(record):
    answer = []
    
    id_nick = dict()
    
    for i in record:
        rec = i.split(" ")
        
        if rec[0] == "Enter" or rec[0] == "Change":
            id_nick.update({rec[1] : rec[2]})
    
    for i in record:
        rec = i.split(" ")
        
        if rec[0] == "Enter":
            answer.append(id_nick[rec[1]] + "님이 들어왔습니다.")
        elif rec[0] == "Leave":
            answer.append(id_nick[rec[1]] + "님이 나갔습니다.")
    
    return answer