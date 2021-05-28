# Pong

Projeto desenvolvido para a disciplina de Redes de Computadores pelas alunas :

* Hellena Almeida Canuto

* Elyssana Maria da Silva Oliveira

  

## Descrição 



A aplicação desenvolvida com uso de Threads, trata-se de um jogo multiplayer para quatro jogadores, sendo duas duplas. Cada jogador controla uma raquete (barra retangular) e cada dupla tem o objetivo de impedir que a bola (circunferência) passe, rebatendo-a com a raquete. Caso a bola passe e bata no fundo, a dupla adversária recebe o ponto. 



## Instruções



Requer Python 3.7.7 ou superior



#### Instalação da biblioteca Pygame:

`python -m pip install -U pygame --user`



#### Alterar IP:

No arquivo “server.py” altere a linha:  `server = "192.168.0.8"`  inserindo seu próprio IPV4

No arquivo “network.py” altere a linha:  `self.server = "192.168.0.8"`  também inserindo seu próprio IPV4

#### Iniciar o servidor da aplicação:

`python server.py `



#### Iniciar quatro instâncias de clientes da aplicação:

Jogador 1 : `python client.py`

Jogador 2 : `python client.py`

Jogador 3 : `python client.py`

Jogador 4 : `python client.py`



#### Iniciar bola do jogo:

`python run_ball.py`


