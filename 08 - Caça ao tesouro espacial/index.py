import random
import os
os.system('clear')


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


print("Bem vindo ao jogo de caça ao tesouro!")
print()

while True:
    numberRandomOne = random.randint(0, 3)
    numberRandomTwo = random.randint(0, 3)
    attempt = 1

    while attempt <= 15:
        try:
            line = int(input("Digite uma linha: "))
            column = int(input("Digite uma coluna: "))
            print()

            if line < 0 or line > 3 or column < 0 or column > 3:
                print('Somente números de 0 a 3 por favor')
                showMap()
                continue

            if map[line][column] == player:
                print("Você já tentou esse, tenta outro!")
                showMap()
                continue

            if line == numberRandomOne and column == numberRandomTwo:
                map[line][column] = treasure
                showMap()
                print("Parabéns você encontrou o tesouro!!!!")
                break
            else:
                map[line][column] = player
                print('Ainda não foi dessa vez tente novamente')
                showMap()
                attempt += 1

            if attempt == 15:
                map[numberRandomOne][numberRandomTwo] = treasure
                print('Fim de jogo! O tesouro estava aqui!!!!')
                showMap()
        except ValueError:
            print('Somente números de 0 a 3, Por Favor...')
            showMap()
            continue

    break
