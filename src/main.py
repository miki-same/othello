from config import *
from board import Othello
from player import Player
from random import randrange

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
            print('WINNER IS BLACK!',end=': ')
        elif winner==WHITE:
            print('WINNER IS WHITE!',end=': ')
        else:
            print('DRAW!',end=': ')
        print(board.stone_count[BLACK]-board.stone_count[WHITE])
        print(board.stone_count[BLACK],board.stone_count[WHITE])
        break


    moves=board.all_legal_hand()
    if board.turn==BLACK:
        move=p.human_search(board)
        h,w=move[0],move[1]
    else:
        #move=p.random_play(board)
        move=p.select_best_move(board)
        h,w=move[0],move[1]
      
    board=board.move(h,w)
