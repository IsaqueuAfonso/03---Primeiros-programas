import os
os.system('clear')

questionsAndAnswers = [
    ["Qual a palavra-chave para definir uma função em Python?", "def"],
    ["Como se chama a estrutura de repetição que executa enquanto uma condição for verdadeira?", "while"],
    ["Qual comando usamos para exibir algo na tela em Python?", "print"]
]
n = 0

print('Vamos jogar um jogo de perguntas e respostas, cada resposta correta vale 1 ponto, sendo um total de 3, vamos lá...')

for i in questionsAndAnswers:
    os.system('clear')
    print(f'{i[0]}')
    print()
    answers = input('A resposta é? ')
    if answers.lower() == i[1]:
        print(f'Reposta está correta')
        n += 1

os.system('clear')
print()
print(f'Sua potuação é: {n}')
