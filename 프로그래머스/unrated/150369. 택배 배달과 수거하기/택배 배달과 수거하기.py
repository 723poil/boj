def solution(cap, n, deliveries, pickups):
    answer = 0
    
    while deliveries or pickups:
        
        while deliveries and deliveries[-1] == 0:
            del deliveries[-1]
        while pickups and pickups[-1] == 0:
            del pickups[-1]
            
        answer += 2 * max(len(deliveries), len(pickups))
        
        can_del = cap
        for idx in reversed(range(len(deliveries))):
            if deliveries[idx] > can_del:
                deliveries[idx] -= can_del
                break
            else:
                can_del -= deliveries[idx]
                deliveries[idx] = 0
                
        can_pku = cap
        for idx in reversed(range(len(pickups))):
            if pickups[idx] > can_pku:
                pickups[idx] -= can_pku
                break
            else:
                can_pku -= pickups[idx]
                pickups[idx] = 0
            
    return answer