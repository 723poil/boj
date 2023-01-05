def solution(id_list, report, k):
    answer = []
    n = len(id_list)
    
    for i in range(n):
        answer.append(0)
        
    reports = {id: 0 for id in id_list}
    
    for i in set(report):
        i = i.split(' ')
        reports[i[1]] += 1

    for i in set(report):
        i = i.split(' ')
        if reports[i[1]] >= k:
            answer[id_list.index(i[0])] += 1
    
    return answer