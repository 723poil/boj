def solution(today, terms, privacies):
    answer = []
    
    ty,tm,td = map(int, today.split("."))
    
    terms_dict = dict()
    
    for term in terms:
        term_list = term.split(" ")
        terms_dict[term_list[0]] = int(term_list[1])
        
    for idx, privacy in enumerate(privacies):
        privacy_list = privacy.split(" ")
        t = privacy_list[1]
        y, m, d = map(int, privacy_list[0].split("."))
        
        if terms_dict[t] >= 12:
            y += terms_dict[t] // 12
            m += terms_dict[t] % 12
        else:
            m += terms_dict[t]
        
        if m > 12:
            y += m // 12
            m = m % 12
            
        privacy_to = ".".join([str(y), str(m), str(d)])

        if y < ty or (y == ty and m < tm) or (y == ty and m == tm and d <= td):
            answer.append(idx+1)

    return answer