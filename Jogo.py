import os

def humanoHumano():

    print("\nVocê selecionou o modo: HUMANO x HUMANO"
          "\nQuem começará jogando?")

    jogador1 = input("\n» Digite o nome do Jogador 1: ")

    print(f"Olá {jogador1}! Contra quem você irá jogar?")

    jogador2 = input("\n» Digite o nome do Jogador 2: ")

    print("Estamos prontos para começar! Selecione uma das opções abaixo para fazer sua jogada."
          "\n1 - pedra"
          "\n2 - papel"
          "\n3 - tesoura")
    
    jogada1 = int(input("Faça sua jogada {jogador1}: "))

    while jogada1 != 1 and jogada1 != 2 and jogada1 != 3:
        print("Você selecionou uma opção INVÁLIDA! Selecione uma das opções abaixo para fazer sua jogada."
          "\n1 - pedra"
          "\n2 - papel"
          "\n3 - tesoura")
        
        jogada1 = int(input("Faça sua jogada {jogador1}: "))


print('OPÇÕES DE JOGO'.center(60))
print('=-'*30)
print('1. JOGAR CONTRA BOT'.center(10))
print('2. JOGAR CONTRA AMIGO'.center(10))
print('3. OBSERVAR DOIS BOTS'.center(10))
print('=-'*30)

c = int(input('Escolha uma opção de jogo: \n'))
if c == 1:
    print('oi')
elif c == 2:
    print('oi')
elif c == 3:
    print('oi')
else:
    print('TENTE DE NOVO, resposta INVALIDA')
    os.system('cls')
    print('limpo')
