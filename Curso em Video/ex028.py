from random import randint
from time import sleep
print(f'\033[33m-=-\033[m'*19)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print(f'\033[33m-=-\033[m'*19)
num = int(input('Em qual número estou pensando? '))
sorte = randint(0, 5)
print('E eu pensei no...')
sleep(3)
print(sorte)
if num == sorte:
    print(f'\033[32mParabéns, você conseguiu acertar!!\033[m')
else:
    print('\033[31mNão foi dessa vez, mais sorte na próxima.\033[m')
#Finalizado com sucesso!