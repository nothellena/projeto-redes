# Pong

Projeto desenvolvido para a disciplina de Redes de Computadores pelas alunas :

* Hellena Almeida Canuto

* Elyssana Maria da Silva Oliveira

  
<br>

## Descrição 


<br>
A aplicação desenvolvida com uso de Threads, trata-se de um jogo multiplayer para quatro jogadores, sendo duas duplas. Cada jogador controla uma raquete (teclas direcionais  "para cima" e "para baixo") e cada dupla tem o objetivo de impedir que a bola passe, rebatendo-a com a raquete. Caso a bola passe e bata no fundo, a dupla adversária recebe o ponto. A primeira dupla a atingir 30 pontos vence a partida.


<hr>

## Instruções
<br>


Requer Python 3.7.7 ou superior



### Instalação da biblioteca Pygame:

`python -m pip install -U pygame --user`

<br>

### Alterar IP:

No arquivo “server.py” altere a linha:  `server = "192.168.0.8"`  inserindo seu próprio IPV4

No arquivo “network.py” altere a linha:  `self.server = "192.168.0.8"`  também inserindo seu próprio IPV4
<br>

### Iniciar o servidor da aplicação:

`python server.py `

<br>

### Iniciar quatro instâncias de clientes da aplicação:

Jogador 1 : `python client.py`

Jogador 2 : `python client.py`

Jogador 3 : `python client.py`

Jogador 4 : `python client.py`

<br>

### Iniciar partida:

`python start_game.py`
<hr>

## Comunicação

Os dados necessários para a execução do jogo, como a posição dos jogadores e da bola e o score são enviados/recebidos em formato de string. Para esse fim, foram desenvolvidas algumas funções auxiliares contidas em ‘utils.py.

<hr>

## O que poderia ter sido implementado a mais

- Diferentes níveis de dificuldades
- rounds de partida
- modo 2-player.


