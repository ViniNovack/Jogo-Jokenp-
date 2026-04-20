# ✊🖐️✌️ Pedra, Papel e Tesoura — Terminal Edition

> Jogo clássico de Pedra, Papel e Tesoura desenvolvido em Python para o terminal, com múltiplos modos de jogo, sistema de pontuação e histórico de partidas.

---

## 📋 Índice

- [Sobre o Projeto](#-sobre-o-projeto)
- [Modos de Jogo](#-modos-de-jogo)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [Como Executar](#-como-executar)
- [Fluxo do Jogo](#-fluxo-do-jogo)
  - [Tela Inicial](#1-tela-inicial--seleção-de-modo)
  - [Modo 1: Jogador vs Bot](#2-modo-1--jogador-vs-bot)
  - [Modo 2: Jogador vs Jogador](#3-modo-2--jogador-vs-jogador)
  - [Modo 3: Bot vs Bot](#4-modo-3--bot-vs-bot)
  - [Tabela de Pontuação e Histórico](#5-tabela-de-pontuação-e-histórico)
- [Integrantes](#-integrantes)

---

## 📖 Sobre o Projeto

Este projeto é uma implementação do clássico jogo **Pedra, Papel e Tesoura** diretamente no terminal do Python. O jogo foi desenvolvido com foco em uma experiência interativa e divertida, utilizando cores no terminal via **ANSI escape codes**, emojis, validação de entradas e múltiplos modos de jogo.

O projeto foi criado como exercício prático de lógica de programação, estruturas de controle e organização de código em Python.

---

## 🎮 Modos de Jogo

| Modo | Descrição |
|---|---|
| 🤖 Jogador vs Bot | Jogue contra uma IA que faz jogadas aleatórias |
| 😀 Jogador vs Jogador | Dois jogadores se alternam na mesma máquina |
| 👾 Bot vs Bot | Assista dois bots se enfrentando |

---

## ✨ Funcionalidades

- 🤖 **Modo Jogador vs Bot** — Enfrente um robô com jogadas aleatórias
- 😀 **Modo Jogador vs Jogador** — Dispute com um amigo no mesmo computador (as jogadas são ocultadas com `getpass` para não haver trapaça!)
- 👾 **Modo Bot vs Bot** — Apenas observe dois bots disputando entre si
- 📊 **Tabela de Pontuação** — Placar final exibido ao término das partidas
- 📜 **Histórico de Partidas** — Registro detalhado de todas as rodadas jogadas
- 🎨 **Interface Colorida** — Cores e emojis para tornar o terminal mais dinâmico
- ✅ **Validação de Entradas** — O jogo detecta entradas inválidas e solicita correção

---

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Bibliotecas:** `random` · `os` · `time` · `getpass`

---

## 🚀 Como Executar

**Pré-requisitos:** Python 3.x instalado.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta do projeto
cd seu-repositorio

# Execute o jogo
python Jogo.py
```

> ⚠️ **Atenção:** O jogo usa `os.system('cls')` para limpar o terminal. Caso esteja no Linux/Mac, substitua `'cls'` por `'clear'` no código.

---

## 🎮 Fluxo do Jogo

### 1. Tela Inicial — Seleção de Modo

Ao iniciar o programa, o jogador é apresentado ao menu principal com as três opções de jogo disponíveis.

```
════════════════════ OPÇÕES DE JOGO ════════════════════
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          1. 🤖 JOGAR CONTRA BOT 🤖
          2. 😀 JOGAR CONTRA AMIGO 😁
          3. 👾 OBSERVAR DOIS BOTS 🤖
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
>>> Escolha uma opção de jogo: _
```

> 📌 **Descrição:** O menu inicial apresenta as três modalidades de jogo. O jogador digita `1`, `2` ou `3` para escolher o modo desejado. Qualquer outro valor resulta em uma mensagem de erro e encerra o programa.

---

### 2. Modo 1 — Jogador vs Bot

O modo mais clássico: o jogador enfrenta um bot com jogadas completamente aleatórias. O bot tem uma personalidade provocativa e comenta cada resultado!

**Etapa 1 — Boas-vindas e início da partida:**
```
Você selecionou o modo: "🤖 JOGAR CONTRA BOT 🤖"
>>> Digite o seu nome:
Ana

Olá Ana!
Eu sou o BOT🤖!, irei ganhar de você!🧐

Vamos COMEÇAR? (Y/N)
> _
```

> 📌 **Descrição:** O jogador informa seu nome e o bot o desafia. A qualquer momento o jogador pode encerrar digitando `N`.

---

**Etapa 2 — Realizando a jogada:**
```
Você pode escolher entre:
1. ✊
2. 🖐️
3. ✌️

😎 FAÇA SUA JOGADA DE VENCEDOR 🤩:
Password: ****

🤖👾Eu joguei papel 🖐️

🤖👾Você é MUITO RUIM, mas não se sinta mal
minhas abilidades podem ser muito intimidadoras 🥱😝🤪
```

> 📌 **Descrição:** A jogada do jogador é digitada de forma **oculta** (usando `getpass`), garantindo que ninguém ao redor veja a escolha. Em seguida, o bot revela sua jogada e o resultado é exibido com uma mensagem temática.

---

**Etapa 3 — Continuação ou encerramento:**
```
Vamos JOGAR MAIS UMA RODADA? (Y/N)
> N

Obrigado por jogar Ana🤗🤩
Foi um prazer conhecer você😝
```

> 📌 **Descrição:** Após cada rodada, o jogador decide se quer continuar. Ao digitar `N`, o jogo encerra a partida e exibe uma mensagem de despedida antes de mostrar o placar.

---

### 3. Modo 2 — Jogador vs Jogador

Dois jogadores humanos disputam no mesmo terminal. As jogadas ficam ocultas para evitar trapaças!

**Etapa 1 — Cadastro dos jogadores:**
```
Você selecionou o modo: HUMANO x HUMANO
Quem começará jogando?

» Digite o nome do Jogador 1: Carlos

Olá Carlos! Contra quem você irá jogar?

» Digite o nome do Jogador 2: Beatriz
```

> 📌 **Descrição:** Ambos os jogadores informam seus nomes antes da partida começar. Isso personaliza todas as mensagens do jogo.

---

**Etapa 2 — Jogadas simultâneas (ocultas):**
```
Estamos prontos para começar! Selecione uma das opções:
1 - pedra
2 - papel
3 - tesoura

Faça sua jogada Carlos:
Password: ****

Faça sua jogada Beatriz:
Password: ****
```

> 📌 **Descrição:** Cada jogador digita sua escolha de forma oculta. O uso do `getpass` impede que o adversário veja a jogada na tela, garantindo uma disputa justa mesmo compartilhando o mesmo teclado.

---

**Etapa 3 — Revelação do resultado:**
```
     ☆ Vitóooria de Carlos! ☆

papel ganha de pedra, Beatriz..

Deseja jogar novamente? (Y/N): _
```

> 📌 **Descrição:** O resultado é exibido com destaque colorido, informando qual jogada venceu e quem perdeu. Em caso de empate, uma mensagem especial aparece.

---

### 4. Modo 3 — Bot vs Bot

O espectador apenas observa dois bots — com personalidades opostas — disputarem entre si em tempo real!

**Etapa 1 — Apresentação dos bots:**
```
Você selecionou o modo: "👾 OBSERVAR DOIS BOTS 🤖"

Olá!
Eu sou o BOT🤖!, irei ganhar da minha irmã que é uma 🤬!🧐

Oiiii!
Eu sou a Bot👾!, meu irmão é meio irritadinho,
mas eu não vou me intimidar com perdedores!🥱😇

Vamos COMEÇAR? (Y/N)
> _
```

> 📌 **Descrição:** Os dois bots se apresentam com personalidades provocativas e rivais entre si, tornando a experiência mais divertida mesmo para quem só observa.

---

**Etapa 2 — Rodada automática:**
```
As jogadas possíveis são:
1. ✊
2. 🖐️
3. ✌️

🤖 Eu joguei tesoura ✌️
👾 Eu joguei pedra ✊

👾Você é REALMENTE MUITO RUIM!!!!
Ainda mais para alguém igual você😘😎
🤖 VOCÊ...🙀😤
👾 Seu silêncio é música para meus ouvidos robóticos😏😎

Vamos JOGAR MAIS UMA RODADA? (Y/N)
> _
```

> 📌 **Descrição:** As jogadas de ambos os bots são geradas aleatoriamente e reveladas uma após a outra. As mensagens de vitória, derrota e empate são dialogadas entre os dois bots, criando uma "briga" cômica.

---

### 5. Tabela de Pontuação e Histórico

Ao final de qualquer modo, o jogo exibe o placar completo e oferece acesso ao histórico detalhado de partidas.

**Tabela de Pontuação:**
```
════════════ ✿ 。TABELA DE PONTUAÇÃO 。✿ ════════════
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          1º Ana😁  4
          2º BOT🤖  2
          📌 Empatamos em 1 rodadas😅
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Deseja acessar seu histórico de partidas? (Y/N)
> Y
```

> 📌 **Descrição:** O placar final classifica os participantes por número de vitórias e exibe o total de empates. O vencedor aparece em primeiro lugar.

---

**Histórico de Partidas:**
```
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
          ✿ 。HISTÓRICO DE PARTIDAS 。✿
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

1 - Ana GANHOU
2 - 🤖 GANHOU
3 - EMPATE
4 - Ana GANHOU
5 - Ana GANHOU
6 - 🤖 GANHOU
7 - Ana GANHOU
```

> 📌 **Descrição:** O histórico lista cada rodada jogada com seu respectivo resultado, com cores diferenciadas para vitória do jogador (verde), vitória do bot (azul) e empate (amarelo). O jogador pode optar por não ver o histórico digitando `N`.

---

## 👥 Integrantes

<table>
  <tr>
    <td align="center">
      <b>Vinícius</b><br/>
      🎮 Desenvolvedor
    </td>
    <td align="center">
      <b>Carol</b><br/>
      🎮 Desenvolvedora
    </td>
  </tr>
</table>

---
