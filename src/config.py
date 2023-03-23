H:int=8
W:int=8
BLACK:int=0
WHITE:int=1
LEGAL:int=2
VACANT:int=3
DIRECTION=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(-1,1),(1,-1)]
ROWS:list[str]=['1','2','3','4','5','6','7','8']
COLUMNS:list[str]=['A','B','C','D','E','F','G','H']


INF:int=10**9


BG='\033[7m'
GREEN_BG = '\033[32m'+BG
BLACK_BG='\033[30m'+BG
WHITE_BG='\033[37m'+BG
YELLOW_BG='\033[33m'+BG
END = '\033[0m'

GREEN_BOARD=GREEN_BG+'.'+END
BLACK_PIECE=BLACK_BG+'x'+END
WHITE_PIECE=WHITE_BG+'o'+END
GREEN_SPACE=GREEN_BG+' '+END
LEGAL_BOARD=YELLOW_BG+'!'+END