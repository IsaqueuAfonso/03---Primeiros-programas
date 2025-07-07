import os
os.system('clear')

print('Olá sou seu Oráculo da sabedoria de programação')
print()
comando = input('Em que assunto posso lhe ajudar? ')

match comando:
    case 'Funções em Python':
        print('Funções em Python permitem organizar o código em blocos reutilizáveis, facilitando a manutenção e a leitura. Você pode definir uma função usando a palavra-chave def e chamá-la sempre que precisar executar aquela tarefa específica.')
    case _:
        print('Desculpe ainda estou aprendendo')
