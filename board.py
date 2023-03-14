from config import *

class Othello:
  def __init__(self,board_state=None,rev=False):
    self.board=[[VACANT for _ in range(W)] for _ in range(H)]
    self.stone_count=dict()
    self.stone_count[BLACK]=0
    self.stone_count[WHITE]=0
    self.turn=BLACK
    self.rev=rev

    if board_state is not None:
      for i in range(H):
        for j in range(W):
          self.board[i][j]=board_state[i][j]
          if board_state[i][j]==BLACK:
            self.stone_count[BLACK]+=1
          elif board_state[i][j]==WHITE:
            self.stone_count[WHITE]+=1
      
      if (self.stone_count[WHITE]+self.stone_count[BLACK])%2:
        self.turn=WHITE

    else:
      self.board[3][3]=WHITE
      self.board[4][4]=WHITE
      self.board[3][4]=BLACK
      self.board[4][3]=BLACK
      self.stone_count[BLACK]=2
      self.stone_count[WHITE]=2  
    
    if self.rev:
      self.turn=self.opponent()
  
  def opponent(self):
    return BLACK if self.turn==WHITE else WHITE

  def print_info(self):
    print('turn: {}'.format('BLACK' if self.turn==BLACK else 'WHITE'))
    print('  A B C D E F G H')
    for i in range(H):
      print(i+1,end=' ')
      for j in range(W):
        c='.'
        if self.board[i][j]==BLACK:
          c='X'
        elif self.board[i][j]==WHITE:
          c='O'
        elif self.legal(i,j):
          c='!'
        print(c,end=' ')
      print()
  
  def all_legal_hand(self):
    hands=[]
    for i in range(H):
      for j in range(W):
        if self.legal(i,j):
          hands.append((i,j))
    
    return hands

  def finish(self):
    new_board=self.move(-1,-1)
    if not self.all_legal_hand() and not new_board.all_legal_hand():
      return True
    else:
      return False
  
  def winner(self):
    if not self.finish():
      return VACANT
    
    if self.stone_count[BLACK]>self.stone_count[WHITE]:
      return BLACK
    elif self.stone_count[BLACK]<self.stone_count[WHITE]:
      return WHITE
    else:
      return VACANT

  def nearest(self,h,w,dh,dw):
    player=self.turn
    h+=dh;w+=dw
    while h>=0 and h<H and w>=0 and w<W:
      if self.board[h][w]==player:
        return h,w
      h+=dh;w+=dw
    
    return -1,-1

  def between(self,h,w,nh,nw,dh,dw)->bool:
    th,tw=h+dh,w+dw

    if th==nh and tw==nw:
      return False

    while not (th==nh and tw==nw):
      if self.board[th][tw]!=self.opponent():
        return False
      th+=dh;tw+=dw
    return True

  def legal(self,h,w)->bool:

    if self.board[h][w]!=VACANT:
      return False

    for dh,dw in DIRECTION:
      nh,nw=self.nearest(h,w,dh,dw)
      if nh==-1:
        continue

      if self.between(h,w,nh,nw,dh,dw):
        return True
      
    return False

  def _flip(self,h,w,nh,nw,dh,dw)->None:
    player=self.turn
    th,tw=h+dh,w+dw
    self.stone_count[self.turn]+=1
    while not (th==nh and tw==nw):
      self.board[th][tw]=player
      self.stone_count[self.turn]+=1
      self.stone_count[self.opponent()]-=1
      th+=dh;tw+=dw
    return

  def move_p(self,h,w):
    if not self.legal(h,w):
      return False

    player=self.turn
    
    self.board[h][w]=player

    for dh,dw in DIRECTION:
      nh,nw=self.nearest(h,w,dh,dw)
      if nh==-1:
        continue
      if self.between(h,w,nh,nw,dh,dw):
        self._flip(h,w,nh,nw,dh,dw)

    self.turn=BLACK if player==WHITE else WHITE

    return True

  def move(self,h,w):
    if h==-1 and w==-1:
      new_board=Othello(self.board,rev=self.rev^1)
      return new_board
    
    else:
      if not self.legal(h,w):
        return self
    
      new_board=Othello(self.board,rev=self.rev)
      new_board.move_p(h,w)

      return new_board