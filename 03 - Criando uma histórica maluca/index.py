import os
os.system('clear')

def historia():
  print("Me diga...")
  input()

  place = input('Um lugar: ')
  famousPerson = input('Uma pessoa famosa: ')
  object1 = input('Um objeto: ')
  color = input('Uma cor: ')
  verb = input('Um verbo: ')
  number = input('Um número: ')

  print()
  print(f"Em {place}, {famousPerson} encontrou um(a) {object1} {color}.")
  print(f"Decidiu então {verb} {number} vezes e tudo mudou para sempre!")

question = input('Vamos criar uma história juntos? (S/N): ')
if question.lower() == 's':
  os.system('clear')
  historia()

else:
  os.system('clear')
  question = input("Tem certeza? (S/N) ")
  
  if question.lower() == 's':
    os.system('clear')
    print()
    question = input('Bora lá vai ser legal, ainda quer sair? (S/N) ')
  if question.lower() == 's':
      os.system('clear')
      print()
      print('Quem perde é tu')
  else:
    os.system('clear')
    historia()