import os
import random

while True:
  randomNumber = random.randint(1, 10)

  os.system('clear')
  print('Pense em um número de 1 a 10')
  input()
  print(f'Seu número é {randomNumber}? 🤔')
  print()

  question = input('S / N ? ')
  if question.lower() == 's':
    break