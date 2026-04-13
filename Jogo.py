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
    pontj = 0
    pontb = 0
    ponte = 0
    cnt = 0


    os.system('cls')
    print('Você selecionou o modo: "🤖JOGAR CONTRA BOT🤖"')
    j1 = str(input('Digite o seu nome: \n'))
    os.system('cls')
    print(f'Olá {j1}! \n''Eu sou o BOT🤖!, irei ganhar de você!🧐 \n')
    while True:
        if cnt == 0:
            cnt +=1
            v1 = str(input('Vamos COMEÇAR? (Y/N)\n'))
            if (v1.lower()).strip() == 'n':
                break
        else:
            time.sleep(2)
            os.system('cls')
            v2 = str(input('Vamos JOGAR MAIS UMA RODADA? (Y/N)\n'))
            if (v2.lower()).strip() == 'n':
                break
      

        os.system('cls')
        print('Você pode escolher entre: \n'
              '1. ✊🏻 \n'
              '2. 🖐🏻 \n'
              '3. ✌🏻')
        while True:
            rj = int(stdiomask.getpass(prompt='😎 FAÇA SUA JOGADA DE VENCEDOR🤩: \n', mask='.'))
            if rj == 1 or rj == 2 or rj == 3:
                break
            else:
                print('Esse valor é INVALIDO😵🥴, tente de novo considerando os números 1, 2 e 3')
                continue


        rb = random.randrange(1, 4)
        if rb == 1:
            print('🤖👾Eu joguei pedra ✊🏻 \n')
        elif rb == 2:
            print('🤖👾Eu joguei papel 🖐🏻 \n')
        elif rb == 3:
            print('🤖👾Eu joguei tesoura ✌🏻 \n')

      
        if rj == rb:
            print(f'😱NOS EMPATAMOS😩, VAMOS MAIS UMA {j1} QUERO GANHAR DE VOCÊ👾🤩😜')
            ponte +=1
            continue
        elif rj == 1 and rb == 3:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            continue
        elif rj == 2 and rb == 1:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            continue
        elif rj == 3 and rb == 2:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            continue
        elif rb == 1 and rj == 3:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            continue
        elif rb == 2 and rj == 1:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            continue
        elif rb == 3 and rj == 2:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            continue
    

    os.system('cls')
    print(f'Obrigado por jogar {j1}🤗🤩 \n'
          'Foi um prazer conhacer você😝')
    time.sleep(4)
    os.system('cls')
    print('TABELA DE PONTUAÇÃO'.center(60))
    print('=-'*30)
    if pontj > pontb:
        print(f'1º {j1}😁 {pontj}'.center(10))
        print(f'2º BOT🤖 {pontb}'.center(10))
        print(f'📌Ematamos em {ponte} rodadas😅'.center(10))
    elif pontj < pontb:
        print(f'1º BOT🤖 {pontb}'.center(10))
        print(f'2º {j1}😢 {pontj}'.center(10))
        print(f'📌Ematamos em {ponte} rodadas😅'.center(10))
    else:
        print(f'1º BOT🤖 {pontb} - {j1}😐 {pontj}'.center(10))
        print(f'📌Ematamos em {ponte} rodadas😅'.center(10))
  

def BotBot():
    pontj = 0
    pontb = 0
    ponte = 0
    cnt = 0


    os.system('cls')
    print('Você selecionou o modo: "👾OBSERVAR DOIS BOTS🤖"')
    time.sleep(0.5)
    os.system('cls')
    print(f'Olá! \n''Eu sou o BOT🤖!, irei ganhar da minha irmã que é uma 🤬!🧐 \n')
    time.sleep(0.5)
    print('Oiiii! \n''Eu sou a Bot👾!, meu irmão é meio iritadinho, mas eu não vou me intimidar com perdedores!🥱😇')
    
    while True:
        if cnt == 0:
            cnt +=1
            v1 = str(input('Vamos COMEÇAR? (Y/N)\n'))
            if (v1.lower()).strip() == 'n':
                break
        else:
            time.sleep(2)
            os.system('cls')
            v2 = str(input('Vamos JOGAR MAIS UMA RODADA? (Y/N)\n'))
            if (v2.lower()).strip() == 'n':
                break
      

        os.system('cls')
        print('As jogadas posiveis são: \n'
              '1. ✊🏻 \n'
              '2. 🖐🏻 \n'
              '3. ✌🏻')
        
        time.sleep(1)
        rb1 = random.randrange(1, 4)
        if rb1 == 1:
            print('🤖Eu joguei pedra ✊🏻')
        elif rb1 == 2:
            print('🤖Eu joguei papel 🖐🏻 \n')
        elif rb1 == 3:
            print('🤖Eu joguei tesoura ✌🏻 \n')

        time.sleep(1)
        rb2 = random.randrange(1, 4)
        if rb2 == 1:
            print('👾Eu joguei pedra ✊🏻 \n')
        elif rb2 == 2:
            print('👾Eu joguei papel 🖐🏻 \n')
        elif rb2 == 3:
            print('👾Eu joguei tesoura ✌🏻 \n')

      
        if rb1 == rb2:
            print(f'😱NOS EMPATAMOS😩, VAMOS MAIS UMA QUERO GANHAR DE VOCÊ👾🤩😜')
            ponte +=1
            continue
        elif rb1 == 1 and rb2 == 3:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            continue
        elif rb1 == 2 and rb2 == 1:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            continue
        elif rb1 == 3 and rb2 == 2:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            continue
        elif rb2 == 1 and rb1 == 3:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            continue
        elif rb2 == 2 and rb1 == 1:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            continue
        elif rb2 == 3 and rb1 == 2:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            continue
    

    os.system('cls')
    print(f'Obrigado por jogar {j1}🤗🤩 \n'
          'Foi um prazer conhacer você😝')
    time.sleep(4)
    os.system('cls')
    print('TABELA DE PONTUAÇÃO'.center(60))
    print('=-'*30)
    if pontj > pontb:
        print(f'1º {j1}😁 {pontj}'.center(10))
        print(f'2º BOT🤖 {pontb}'.center(10))
        print(f'📌Ematamos em {ponte} rodadas😅'.center(10))
    elif pontj < pontb:
        print(f'1º BOT🤖 {pontb}'.center(10))
        print(f'2º {j1}😢 {pontj}'.center(10))
        print(f'📌Ematamos em {ponte} rodadas😅'.center(10))
    else:
        print(f'1º BOT🤖 {pontb} - {j1}😐 {pontj}'.center(10))
        print(f'📌Ematamos em {ponte} rodadas😅'.center(10))


import random
import os       #(LIMPA O TERMINAL) (os.system('cls'))
import stdiomask  #(ESCREVE IGUAL SENHA) (stdiomask.getpass(prompt='Escolha uma opção de jogo: \n', mask='.'))
import time


print('OPÇÕES DE JOGO'.center(60))
print('=-'*30)
print('1. 🤖JOGAR CONTRA BOT🤖'.center(10))
print('2. JOGAR CONTRA AMIGO'.center(10))
print('3. 👾OBSERVAR DOIS BOTS🤖'.center(10))
print('=-'*30)


c = int(input('Escolha uma opção de jogo: \n'))
if c == 1:
    humanoBot()
elif c == 2:
    print('oi')
elif c == 3:
    BotBot()
else:
    print('❌TENTE DE NOVO, resposta INVALIDA❌')
