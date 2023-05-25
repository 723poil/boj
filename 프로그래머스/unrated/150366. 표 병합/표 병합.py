def solution(commands):
    R = 51
    C = 51
    answer = []
    rcval = [['' for _ in range(C)] for _ in range(R)]
    rcgrp = [[(r, c) for c in range(C)] for r in range(R)]
    
    def find(r, c):
        while rcgrp[r][c] != (r, c):
            r, c = rcgrp[r][c]
        return r, c
            
    #"UPDATE r c value"
    def update_r_c_value(r, c, value):
        r, c = find(r, c)
        rcval[r][c] = value

    #"UPDATE value1 value2"
    def update_value1_value2(v1, v2):
        for r in range(R):
            for c in range(C):
                pr, pc = find(r, c)
                if rcval[pr][pc] == v1:
                    rcval[pr][pc] = v2
                
    #"MERGE r1 c1 r2 c2"
    def merge_r1_c1_r2_c2(r1, c1, r2, c2):
        pr1, pc1 = find(r1, c1)
        pr2, pc2 = find(r2, c2)
        
        if pr1 == pr2 and pc1 == pc2:
            return
        val = rcval[pr1][pc1] or rcval[pr2][pc2]
        
        if pr1+pc1 < pr2+pc2 or (pr1+pc1 == pr2+pc2 and pr1 < pr2):
            rcgrp[pr2][pc2] = (pr1, pc1)
            rcval[pr1][pc1] = val
        else:
            rcgrp[pr1][pc1] = (pr2, pc2)
            rcval[pr2][pc2] = val

    #"UNMERGE r c"
    def unmerge_r_c(r, c):
        pr, pc = find(r, c)
        val = rcval[pr][pc]
        group = {(pr, pc)}
        while group:
            new_group = set()
            for row in range(R):
                for col in range(C):
                    rr, cc = find(row, col)
                    if (rr, cc) in group:
                        if (row, col) not in group:
                            new_group.add((row, col))
                        rcval[row][col] = ''
                        rcgrp[row][col] = (row, col)
            group = new_group
        rcval[r][c] = val

    #"PRINT r c"
    def print_r_c(r, c):
        r, c = find(r, c)
        return rcval[r][c] or "EMPTY"
    
    for command in commands:
        command = command.split(" ")
        
        if command[0] == "UPDATE":
            if len(command) == 3:
                _, v1, v2 = command
                update_value1_value2(v1, v2)
            else:
                _, r, c, value = command
                update_r_c_value(int(r), int(c), value)
        elif command[0] == "MERGE":
            _, r1, c1, r2, c2 = command
            merge_r1_c1_r2_c2(int(r1), int(c1), int(r2), int(c2))
        elif command[0] == "UNMERGE":
            _, r, c = command
            unmerge_r_c(int(r), int(c))
        else:
            _, r, c = command
            answer.append(print_r_c(int(r), int(c)))
    
    return answer