from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
escolha = int(input('''Escolha o que vai jogar:
[0] Pedra
[1] Papel
[2] Tesoura
Qual é a sua jogada? '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 10)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[escolha]}')
print('-=' * 10)

if computador == 0:
    if escolha == 0:
        print('Empate')
    elif escolha == 1:
        print('O Jogador Venceu!')
    else:
        print('O Computador Venceu!')

elif computador == 2:
    if escolha == 2:
        print('Empate')
    elif escolha == 0:
        print('O Jogador Venceu!')
    else:
        print('O Computador Venceu!')

elif computador == 1:
    if escolha == 1:
        print('Empate')
    elif escolha == 2:
        print('O Jogador Venceu!')
    else:
        print('O Computador Venceu!')
