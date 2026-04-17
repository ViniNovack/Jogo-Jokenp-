import random
import os       #(LIMPA O TERMINAL) (os.system('cls'))
import time
import getpass

class Cores:
    # Cores de texto para o terminal
    branco = '\033[30m'
    vermelho = '\033[31m'
    verde = '\033[32m'
    amarelo = '\033[33m'
    azul = '\033[34m'
    magenta = '\033[35m'
    ciano = '\033[36m'
    cinza = '\033[37m'

    # Cores de fundo para o terminal
    fundo_preto = '\033[40m'
    fundo_vermelho = '\033[41m'
    fundo_verde = '\033[42m'
    fundo_amarelo = '\033[43m'
    fundo_azul = '\033[44m'
    fundo_magenta = '\033[45m'
    fundo_ciano = '\033[46m'
    fundo_branco = '\033[47m'

    # LIMPAR
    limpar = '\033[m'


print('OPÇÕES DE JOGO'.center(60))
print('=-'*30)
print('1. 🤖 JOGAR CONTRA BOT 🤖'.center(10))
print('2. 😀 JOGAR CONTRA AMIGO 😁'.center(10))
print('3. 👾 OBSERVAR DOIS BOTS 🤖'.center(10))
print('=-'*30)


c = int(input('Escolha uma opção de jogo: '))

if c == 1: # humanoBot()
    pontj = 0
    pontb = 0
    ponte = 0
    cnt = 0
    tabela = ''
    i = 0

    os.system('cls')
    print('Você selecionou o modo: "🤖 JOGAR CONTRA BOT 🤖"')
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
        i +=1
        print('Você pode escolher entre: \n'
              '1. ✊ \n'
              '2. 🖐️ \n'
              '3. ✌️')
        while True:
            rj = int((getpass.getpass('😎 FAÇA SUA JOGADA DE VENCEDOR 🤩: \n')))
            if rj == 1 or rj == 2 or rj == 3:
                break
            else:
                print('Esse valor é INVALIDO😵🥴, tente de novo considerando os números 1, 2 e 3')
                continue


        rb = random.randrange(1, 4)
        if rb == 1:
            print('🤖👾Eu joguei pedra ✊ \n')
        elif rb == 2:
            print('🤖👾Eu joguei papel 🖐️ \n')
        elif rb == 3:
            print('🤖👾Eu joguei tesoura ✌️ \n')

        if rj == rb:
            print(f'😱NOS EMPATAMOS😩, VAMOS MAIS UMA {j1} QUERO GANHAR DE VOCÊ👾🤩😜')
            ponte +=1
            tabela += f'{i} - EMPATE\n'
            continue
        elif rj == 1 and rb == 3 or rj == 2 and rb == 1 or rj == 3 and rb == 2:
            print('🤖👾Você ganhou de mim!😡🤬😫,VAMOS MAIS UMA RODADA!!!')
            pontj +=1
            tabela += f'{i} - {j1} GANHOU\n'
            continue

        elif rb == 1 and rj == 3 or rb == 2 and rj == 1 or rb == 3 and rj == 2:
            print('🤖👾Você é MUITO RUIM, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪')
            pontb +=1
            tabela += f'{i} - 🤖 GANHOU\n'
            continue

    

    os.system('cls')
    print(f'Obrigado por jogar {j1}🤗🤩 \n'
          'Foi um prazer conhacer você😝')
    time.sleep(4)
    os.system('cls')
    print('✿ 。TABELA DE PONTUAÇÃO 。✿'.center(60))
    print('=-'*30)
    if pontj > pontb:
        print(f'1º {j1}😁 {pontj}'.center(10))
        print(f'2º BOT🤖 {pontb}'.center(10))
        print(f'📌Epatamos em {ponte} rodadas😅'.center(10))
    elif pontj < pontb:
        print(f'1º BOT🤖 {pontb}'.center(10))
        print(f'2º {j1}😢 {pontj}'.center(10))
        print(f'📌Epatamos em {ponte} rodadas😅'.center(10))
    else:
        print(f'1º BOT🤖 {pontb} - {j1}😐 {pontj}'.center(10))
        print(f'📌Epatamos em {ponte} rodadas😅'.center(10))
    
    t = str(input('Deseja acessar seu historico de partidas? (S/N)\n'))
    if (t.lower()).strip() == 's':
        print('=-'*30)
        print('✿ 。HISTÓRICO DE PARTIDAS 。✿'.center(60))
        print('=-'*30)
        print(tabela)
    else:
        print('Obrigado por jogar!')

elif c == 2: # humanoHumano()
    
    i = 0
    rodadas = ""
    pontE = 0
    pontV1 = 0
    pontV2 = 0

    print("\nVocê selecionou o modo: HUMANO x HUMANO"
          "\nQuem começará jogando?")

    j1 = input("\n» Digite o nome do Jogador 1: ")

    print(f"\nOlá {j1}! Contra quem você irá jogar?")

    j2 = input("\n» Digite o nome do Jogador 2: ")

    while True:
        i += 1

        print("\nEstamos prontos para começar! Selecione uma das opções abaixo para fazer sua jogada."
            "\n1 - pedra"
            "\n2 - papel"
            "\n3 - tesoura")
        
        jogada1 = (getpass.getpass(f"\nFaça sua jogada {j1}: "))

        # Verficação ----------------------------------------------

        while True:
            if jogada1.isdigit():
                jogada1 = int(jogada1)

                if jogada1 != 1 and jogada1 != 2 and jogada1 != 3:
                    print("\nVocê selecionou uma opção INVÁLIDA! Selecione uma das opções abaixo para fazer sua jogada."
                            "\n\n1 - pedra"
                            "\n2 - papel"
                            "\n3 - tesoura")
            
                    jogada1 = (getpass.getpass(f"\nFaça sua jogada {j1}: "))
                else:
                    break
            else:
                print("\nVocê selecionou uma opção INVÁLIDA! Selecione uma das opções abaixo para fazer sua jogada."
                            "\n\n1 - pedra"
                            "\n2 - papel"
                            "\n3 - tesoura")
            
                jogada1 = (getpass.getpass(f"\nFaça sua jogada {j1}: "))
    

        jogada2 = (getpass.getpass(f"\nAgora é sua vez {j2}, faça sua jogada: "))

        while True:
            if jogada2.isdigit():
                jogada2 = int(jogada2)

                if jogada2 != 1 and jogada2 != 2 and jogada2 != 3:
                    print("\nVocê selecionou uma opção INVÁLIDA! Selecione uma das opções abaixo para fazer sua jogada."
                            "\n\n1 - pedra"
                            "\n2 - papel"
                            "\n3 - tesoura")
            
                    jogada2 = (getpass.getpass(f"\nFaça sua jogada {j2}: "))
                else:
                    break
            else:
                print("\nVocê selecionou uma opção INVÁLIDA! Selecione uma das opções abaixo para fazer sua jogada."
                            "\n\n1 - pedra"
                            "\n2 - papel"
                            "\n3 - tesoura")
            
                jogada2 = (getpass.getpass(f"\nFaça sua jogada {j2}: "))

            # -----------------------------------------------------------------
        
        if jogada1 == 1:
            jogada1Tipo = "pedra"
        elif jogada1 == 2:
            jogada1Tipo = "papel"
        else:
            jogada1Tipo = "tesoura"

        if jogada2 == 1:
            jogada2Tipo = "pedra"
        elif jogada2 == 2:
            jogada2Tipo = "papel"
        else:
            jogada2Tipo = "tesoura"
        
        
        if jogada1 == jogada2:

            print(f"\n» EMPATE «".center(40))
            print(f"\nQue fofinhos, vocês pensam igual! Ambos jogaram {jogada1Tipo}!")

            rodadas += f"\n• {i} - Empate"

            pontE += 1
        elif (jogada1 == 1 and jogada2 == 3) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 3 and jogada2 == 2):
            print(f"\n☆ Vitóooria de {j1}! ☆".center(40))
            print(f"\n{jogada1Tipo} ganha de {jogada2Tipo}, {j2}..")

            pontV1 += 1
            rodadas += f"\n• {i} - Vitória de ☆ {j1} ☆"

        else:
            print(f"\n☆ Vitóooria de {j2}! ☆".center(40))
            print(f"\n{jogada2Tipo} ganha de {jogada1Tipo}, {j1}..")

            pontV2 += 1
            rodadas += f"\n• {i} - Vitória de ☆ {j2} ☆"

        jogarNovamente = input("\nDeseja jogar novamente? (s/n): ")
        print(jogarNovamente)

        while jogarNovamente.lower() != "s" and jogarNovamente.lower() != "n":
            jogarNovamente = input("\nOpção inválida. Deseja jogar novamente? (s/n): ")
        
        if jogarNovamente.lower() == "n":
            time.sleep(1)
            os.system('cls')
            print("RESULTADOS".center(60))
            print(f"\n→ {j1} • {pontV1} X {pontV2} • {j2}\n→ Empates: {pontE}")

            opcao = input("\nDeseja acessar o histórico de partidas? (s/n): ")

            while opcao != "n" and opcao != "s":
                opcao = input("\nOpção inávlida. Deseja acessar o histórico de partidas? (s/n): ")

            if opcao == "s":
                print('-'*60)
                print("✿ 。HISTÓRICO DE PARTIDAS 。✿".center(60))
                print(rodadas) 
                print('-'*60)
            break
        else:
            print("\nBora pra mais uma!")
            time.sleep(2)
            os.system('cls')
            
elif c == 3: # BotBot()
    pontj = 0  #🤖
    pontb = 0  #👾
    ponte = 0
    cnt = 0
    tabela = ''
    i = 0
    os.system('cls')
    print('Você selecionou o modo: "👾 OBSERVAR DOIS BOTS 🤖"')
    time.sleep(1)
    os.system('cls')
    print(f'Olá! \n''Eu sou o BOT🤖!, irei ganhar da minha irmã que é uma 🤬!🧐 \n')
    time.sleep(1)
    print('Oiiii! \n''Eu sou a Bot👾!, meu irmão é meio iritadinho, mas eu não vou me intimidar com perdedores!🥱😇')
    
    while True:
        if cnt == 0:
            cnt +=1
            while True:
                v1 = str(input('Vamos COMEÇAR? (Y/N)\n'))
                if (v1.lower()).strip() == 'y' or (v1.lower()).strip() == 'n':
                    break
                else:
                    print('Resposta inválida. Por favor, digite Y ou N\n')
                    continue
            
        if (v1.lower()).strip() == 'n':
            break
        else:
            time.sleep(2)
            os.system('cls')
            v2 = str(input('Vamos JOGAR MAIS UMA RODADA? (Y/N)\n'))
            if (v2.lower()).strip() == 'n':
                break
      

        os.system('cls')
        i +=1
        print('As jogadas posiveis são: \n'
              '1. ✊ \n'
              '2. 🖐️ \n'
              '3. ✌️')
        
        time.sleep(1)
        rb1 = random.randrange(1, 4)
        if rb1 == 1:
            print('🤖Eu joguei pedra ✊')
        elif rb1 == 2:
            print('🤖Eu joguei papel 🖐️ \n')
        elif rb1 == 3:
            print('🤖Eu joguei tesoura ✌️ \n')

        time.sleep(1)
        rb2 = random.randrange(1, 4)
        if rb2 == 1:
            print('👾Eu joguei pedra ✊\n')
        elif rb2 == 2:
            print('👾Eu joguei papel 🖐️ \n')
        elif rb2 == 3:
            print('👾Eu joguei tesoura ✌️ \n')

      
        if rb1 == rb2:
            print('😱NOS EMPATAMOS😩, 🤖VAMOS MAIS UMA QUERO GANHAR DE VOCÊ🤩😜')
            time.sleep(1)
            print('👾FICA CALMINHO, PORQUE PERDEDOR NÃO TEM LUGAR DE FALA🥱😎')
            time.sleep(1)
            print('🤖 😲')
            ponte +=1
            tabela += f'{i} - 👾EMPATE🤖\n'
            continue
        elif rb1 == 1 and rb2 == 3 or rb1 == 2 and rb2 == 1 or rb1 == 3 and rb2 == 2:
            print('🤖GANHEI🤩😎😘!!!!!''QUEM É O PERDEDOR AGORA🙄😏😈')
            time.sleep(1)
            print('👾Você ganhou de mim!😡🤬😫''🙏🏻VAMOS MAIS UMA RODADA!!!')
            time.sleep(1)
            print('🤖FICO IRITADINHA😴🤪🥴')
            pontj +=1
            tabela += f'{i} - 🤖 GANHOU\n'
            continue
        elif rb2 == 1 and rb1 == 3 or rb2 == 2 and rb1 == 1 or rb2 == 3 and rb1 == 2:
            print('👾Você é REALMENTE MUITO RUIM !!!!, mas não se sinta mal minhas abilidades podem ser muito intimidadoras 🥱😝🤪'
                  'Ainda mais para alguém igual você😘😎')
            time.sleep(1)
            print('🤖VOCÊ...🙀😤')
            time.sleep(1)
            print('👾Seu silencio é musica para meus ouvidos roboticos😏😎')
            pontb +=1
            tabela += f'{i} - 👾 GANHOU\n'
            continue

    os.system('cls')
    print(f'🤖👾Obrigado por deixar a gente jogar🤗🤩 \n')
    time.sleep(4)
    os.system('cls')
    print('✿ 。TABELA DE PONTUAÇÃO 。✿'.center(60))
    print('=-'*30)
    if pontj > pontb:
        print(f'1º 😎 BOT🤖 {pontj}'.center(10))
        print(f'2º 😒 BOT👾 {pontb}'.center(10))
        print(f'📌Epatamos em {ponte} rodadas😅'.center(10))
    elif pontj < pontb:
        print(f'1º 😘 BOT👾 {pontb}'.center(10))
        print(f'2º 🤬 BOT🤖 {pontj}'.center(10))
        print(f'📌Epatamos em {ponte} rodadas😅'.center(10))
    else:
        print(f'1º 😕 BOT🤖 {pontj} - 😐 BOT👾 {pontb}'.center(10))
        print(f'📌Epatamos em {ponte} rodadas😅'.center(10))

    t = str(input('Você quer ver o histórico de partidas? (S/N) '))
    if (t.lower()).strip() == 's':
        print('=-'*30)
        print('✿ 。HISTÓRICO DE PARTIDAS 。✿'.center(60))
        print('=-'*30)
        print(tabela)
    else:
        print('Obrigado por jogar!')

else:
    print('❌TENTE DE NOVO, resposta INVALIDA❌')
