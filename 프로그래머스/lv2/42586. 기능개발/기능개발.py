def solution(progresses, speeds):
    
    complete = []
    
    for pro, spd in zip(progresses, speeds):
        if len(complete) == 0 or complete[-1][0] < -((pro-100)//spd):
            complete.append([-((pro-100)//spd), 1])
        else:
            complete[-1][1] += 1
        
    return [com[1] for com in complete]