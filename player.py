from config import *
from board import Othello

class Player:
    def __init__(self):
        self.points=[
            [30,-12,0,-1,-1,0,-12,30],
            [-12,-15,-3,-3,-3,-3,-15,-12],
            [0,-3,0,-1,-1,0,-3,0],
            [-1,-3,-1,-1,-1,-1,-3,-1],
            [-1,-3,-1,-1,-1,-1,-3,-1],
            [0,-3,0,-1,-1,0,-3,0],
            [-12,-15,-3,-3,-3,-3,-15,-12],
            [30,-12,0,-1,-1,0,-12,30]
        ]
    
    def eval_func(self,board:Othello):
        if board.finish():
            winner=board.winner()
            if winner==BLACK:
                return INF
            elif winner==WHITE:
                return -INF
            else:
                return 0
            
        res=0
        for i in range(H):
            for j in range(W):
                if board.board[i][j]==BLACK:
                    res+=self.points[i][j]
                elif board.board[i][j]==WHITE:
                    res-=self.points[i][j]
        return res
  

    def one_move_search(self,board:Othello):
        moves=board.all_legal_hand()
        best_move=(-1,-1)
        best_value=-INF if board.turn==BLACK else INF

        for h,w in moves:
            new_board=board.move(h,w)
            new_value=self.eval_func(new_board)

            if board.turn==BLACK:
                if new_value>=best_value:
                    best_value=new_value
                    best_move=(h,w)
            else:
                if new_value<=best_value:
                    best_value=new_value
                    best_move=(h,w)
        
        return best_move