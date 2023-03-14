from config import *
from board import Othello
from player import Player
from random import randrange

def str_to_move(s:str):
  if s=="PASS":
     return (-1,-1)
  
  if len(s)!=2:
      return (100,100)
  
  h=ROWS.index(s[0])
  w=COLUMNS.index(s[1])

  return h,w


p=Player()
board=Othello()

while True:
    #画面クリア
    print("\x1b[2J\x1b[H\x1b[?25l")
    
    #画面描画
    board.print_info()

    if board.finish():
        winner=board.winner()
        if winner==BLACK:
            print('WINNER IS BLACK!')
        elif winner==WHITE:
            print('WINNER IS WHITE!')
        else:
            print('DRAW!')
        break


    moves=board.all_legal_hand()+[(-1,-1)]
    while True:
      print('Your Turn:')
      print('Legal moves:','PASS',end=', ')
      for move in moves:
         print(ROWS[move[0]]+COLUMNS[move[1]],end=', ')
      print()
      h,w=str_to_move(input())
      
      if not (h,w) in moves:
          print('illegal hand')
          continue
      else:
          break
      
    board=board.move(h,w)
