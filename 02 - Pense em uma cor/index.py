import os
import random

colors = ['azul']

os.system('clear')

while True:
  amount = len(colors)
  randomNumber = random.randint(0, amount - 1)
  print(randomNumber)

  os.system('clear')
  print('Pense em uma cor...')
  input()
  print(f'Sua cor é {colors[randomNumber]}? 🤔')
  print()

  question = input('S / N ? ')
  if question.lower() == 'n':
    color = input('Qual cor você pensou? ')
    if color not in colors:
        colors.append(color.lower())
  elif question.lower() == 's':
    break