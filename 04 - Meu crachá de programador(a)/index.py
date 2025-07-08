import os

print("Vamos fazer seu Crachá Dev")
input()

os.system('clear')

while True:
    name = input("Me diga seu nome: ")
    age = input("Me diga sua idade: ")
    favoriteLanguage = input("Me diga sua linguagem de programação favorita: ")
    emojiThatRepresentsYou = input("Me diga um emoji que te representa: ")
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    print('👩‍💻 Crachá do Dev')
    print(f'Nome: {name}')
    print(f'Idade: {age}')
    print(f'Linguagem favorita: {favoriteLanguage}')
    print(f'Emoji: {emojiThatRepresentsYou}')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

    question = input(f'Quer fazer novamente? (s/n)')
    if question.lower() == 'n':
        break
