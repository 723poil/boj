def solution(board, moves):
    
    moved_board = []
    answer = 0
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                moved_board.append(board[j][i-1])
                board[j][i-1] = 0
                break

        n = len(moved_board)
        
        if n > 1:
            if moved_board[-2] == moved_board[-1]:
                moved_board.pop(-1)
                moved_board.pop(-1)
                answer += 2
        
    return answer