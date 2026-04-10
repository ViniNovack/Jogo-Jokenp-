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


def humanoBot():
    tabj = 0
    tabb = 0


    os.system('cls')
    cnt = 0
    print('Você selecionou o modo: "JOGAR CONTRA BOT"\n')
    j1 = str(input('Digite o seu nome: \n'))
    print(f'Olá {j1}! \n''Eu sou o BOT🤖!, irei ganhar de você!🧐\n')
    while True:
        if cnt == 0:
            cnt +=1
            v1 = str(input('Vamos COMEÇAR? (Y/N)\n'))
            if (v1.lower()).strip() == 'n':
                break
        else:
            v2 = str(input('Vamos JOGAR MAIS UMA RODADA? (Y/N)\n'))
            if (v2.lower()).strip() == 'n':
                break
      
      
        print('Você pode escolher entre: \n'
              '1. ✊🏻'
              '2. 🖐🏻'
              '3. ✌🏻')
        rj = int(stdiomask.getpass(prompt='😎 FAÇA SUA JOGADA DE VENCEDOR 🤩: \n', mask='.'))
        rb = random.randrange(1, 4)
        if rb == 1:
            print('🤖👾Eu joguei pedra ✊🏻 \n')
        elif rb == 2:
            print('🤖👾Eu joguei papel 🖐🏻 \n')
        elif rb == 3:
            print('🤖👾Eu joguei tesoura ✌🏻 \n')

      
        if rj == rb:
            print(f'😱NOS EMPATAMOS😩, VAMOS MAIS UMA {j1} QUERO GANHAR DE VOCÊ👾🤩😜')
            continue
        elif rj == 1 and rb == 3:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            tabj +=1
            continue
        elif rj == 2 and rb == 1:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            tabj +=1
            continue
        elif rj == 3 and rb == 2:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            tabj +=1
            continue
        elif rb == 1 and rj == 3:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            tabj +=1
            continue
        elif rb == 2 and rj == 1:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            tabj +=1
            continue
        elif rb == 3 and rj == 2:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            tabj +=1
            continue

import random
import os       #(LIMPA O TERMINAL) (os.system('cls'))
import stdiomask  #(ESCREVE IGUAL SENHA) (stdiomask.getpass(prompt='Escolha uma opção de jogo: \n', mask='.'))

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
