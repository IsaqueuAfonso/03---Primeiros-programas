import os
import random

os.system('clear')

print('Bem Vindo ao Jogo de Adivinhação.')
input()

while True:
    os.system('clear')
    randomNumber = random.randint(1, 10)

    prohibited = input('O número que estou pensando é... : ')

    number = int(prohibited)
    if number < 1 or number > 10 or not prohibited.isdigit():
        print('Digite um valor númerico de 1 a 10')
        input()
        continue

    if randomNumber == number:
        os.system('clear')
        print('Parabéns você acertou')
        input()
    else:
        os.system('clear')
        print('Não foi dessa vez')
        input()

    os.system('clear')
    playAgain = input('Jogar novamente? (S/N) ')
    if playAgain.lower() == 'n':
        break
