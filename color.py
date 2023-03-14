import time
for i in range(10):
  print("\x1b[2J\x1b[H\x1b[?25l")
  print("\x1b[H")
  print(i)
  time.sleep(1)