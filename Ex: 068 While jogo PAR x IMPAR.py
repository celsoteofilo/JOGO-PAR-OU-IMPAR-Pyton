'''
Faca um programa que joque PAR ou IMPAR com o computador .
O jogador sera interropido quando o jogador perder .
Mostrando o total de vitorias consecutivas , que ele conquiastou ate o final do JOGO .
'''

#--------------------------------------- 1 PARTE ---------------------------------------------------------
from random import  randint

vitoria = 0

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Escolha  Par ou Impar [P/I]: ')).upper()
    print(f'Voce jogou {jogador}, computador {computador}, e total {total}')
#--------------------------------------2 PARTE ------------------------------------------------------------


    if tipo == 'P':
        if total % 2 == 0:
            print('PAR, VENCEU!!')
            vitoria = vitoria + 1
        else:
            print(' VOCE PERDEU ')
            break


    elif tipo == 'I':
        if total % 2 == 1:
            print('Impar, VENCEU !!!')
            vitoria = vitoria + 1
        else:
            print('VOCE PERDEU')
            break
#------------------------------------------------3 PARTE ----------------------------------------------------

    print('Vamos jogar novamete ? ')
#------------------------------------------------- 4 PARTE --------------------------------------------
print(f'Voce Ganhou do Computador {vitoria} vezes .')
print('FIM')

# Jogo simples feito em pythom pois estou aprendendo .












