from random import choice
from time import sleep

escolha = int(input('\033[35m       Jokenpô\033[m '
                    '\nEscolha sua jogada: \n1 - Pedra \n2 - Papel \n3 - Tesoura \nOpção: '))
jogadas = ['Pedra', 'Papel', 'Tesoura']
usu = jogadas[escolha - 1]
jogada_computador = choice(jogadas)

sleep(0.5)
print('\033[33mJo\033[m')
sleep(0.5)
print('\033[36m   Ken\033[m')
sleep(0.5)
print('\033[34m        Po\033[m')

#Empate
if usu == jogada_computador:
    print(f'Sua Jogada: {usu}'
          f'\nCompiuter Jogada: {jogada_computador}'
          f'\n\033[33mEMPATE\033[m')

#Vitória
elif escolha == 1 and jogada_computador == 'Tesoura' \
        or escolha == 2 and jogada_computador == 'Pedra' \
        or escolha == 3 and jogada_computador == 'Papel':
    print(f'Sua Jogada: {usu}'
          f'\nCompiuter Jogada: {jogada_computador}'
          f'\n\033[32mVITÓRIA\033[m')

#Derrota
else:
    print(f'Sua Jogada: {usu}'
          f'\nCompiuter Jogada: {jogada_computador}'
          f'\n\033[31mDERROTA\033[m')
#Finalizado com sucesso!
