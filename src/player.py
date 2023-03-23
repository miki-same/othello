from config import *
from board import Othello

import random

class Player:
    def __init__(self):
        '''
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
        '''
        self.points=[
            [100,-40,20,5,5,20,-40,100],
            [-40,-80,-1,-1,-1,-1,-80,-40],
            [20,-1,5,1,1,5,-1,20],
            [5,-1,1,0,0,1,-1,5],
            [5,-1,1,0,0,1,-1,5],
            [20,-1,5,1,1,5,-1,20],
            [-40,-80,-1,-1,-1,-1,-80,-40],
            [100,-40,20,5,5,20,-40,100],
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
    
    def select_best_move(self,board:Othello):
        moves=board.all_legal_hand()
        best_value=-INF if board.turn==BLACK else INF
        best_move=(-1,-1)

        for h,w in moves:
            new_board=board.move(h,w)
            new_value=self.minimax_search(new_board)

            if best_move==(-1,-1):
                best_value=new_value
                best_move=(h,w)
                continue

            if board.turn==BLACK:
                if new_value>=best_value:
                    best_value=new_value
                    best_move=(h,w)
            else:
                if new_value<=best_value:
                    best_value=new_value
                    best_move=(h,w)

        return best_move

    def minimax_search(self,board:Othello,depth=3):
        
        if depth==0:
            return self.eval_func(board)

        moves=board.all_legal_hand()
        best_value=-INF if board.turn==BLACK else INF

        for h,w in moves:
            new_board=board.move(h,w)
            new_value=self.minimax_search(new_board,depth=depth-1)

            if board.turn==BLACK:
                if new_value>=best_value:
                    best_value=new_value
            else:
                if new_value<=best_value:
                    best_value=new_value
        
        return best_value

    def random_play(self,board:Othello):
        moves=board.all_legal_hand()
        if not moves:
            return (-1,-1)
        
        return moves[random.randrange(len(moves))]

    def str_to_move(self,s:str):
      if s=="PASS":
         return (-1,-1)
    
      if len(s)!=2:
          return (100,100)
    
      h=ROWS.index(s[0])
      w=COLUMNS.index(s[1])
    
      return h,w
    
    def human_search(self,board:Othello):
        while True:
            moves=board.all_legal_hand()
            print('Your Turn:')

            if not moves:
                print('Legal moves: PASS')
            else:
                print('Legal moves:','PASS',end=', ')
            for move in moves:
               print(ROWS[move[0]]+COLUMNS[move[1]],end=', ')
            print()
            h,w=self.str_to_move(input())    
            if not (h,w) in moves and (h,w)!=(-1,-1):
                print('illegal hand')
                continue
            else:
                break
        return (h,w)