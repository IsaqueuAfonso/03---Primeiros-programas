import os

jogos = [
    "01 - Adivinhe o número/index.py",
    "02 - Pense em uma cor/index.py",
    "03 - Criando uma histórica maluca/index.py",
    "05 - Oráculo da sabedoria Python/index.py",
    "06 - Quiz de perguntas e respostas/index.py",
    "07 - Número secreto/index.py",
    "08 - Caça ao tesouro espacial/index.py"
]

for jogo in jogos:
    print(f"\nExecutando: {jogo}\n")
    os.system(f'python3 "{jogo}"')
    input("\nPressione Enter para ir para o próximo jogo...")
