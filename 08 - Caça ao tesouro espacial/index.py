import os
os.system('clear')

import random

map = [
  ['  ', '  ', '  ', '  '],
  ['  ', '  ', '  ', '  '],
  ['  ', '  ', '  ', '  '],
  ['  ', '  ', '  ', '  '],
]
player = 'NO'
treasure = '💎'

def showMap():
  for linha in map:
    print(' | '.join(linha))
    print('-' * 18)

while True:
  numberRandomOne = random.randint(0, 3)
  numberRandomTwo = random.randint(0, 3)

  for attempt in range(1,16):
    line = int(input("Digite uma linha: "))
    column = int(input("Digite uma coluna: "))
    map[line][column] = player
    showMap()
  
  break