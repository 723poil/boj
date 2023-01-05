def solution(participant, completion):
    
    dict = {}
    
    for i in completion:
        if dict.get(i) is None:
            dict.update({i: 1})
        else:
            dict.update({i: dict[i] + 1})
            
    for i in participant:
        if dict.get(i) is None:
            return i
        elif dict[i] != 0:
            dict[i] -= 1
        else:
            return i