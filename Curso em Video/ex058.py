from random import randint
print(f'\033[33m-=-\033[m'*19)
print('\033[35mVou pensar em um número entre 0 e 10. Tente adivinhar...\033[m')
print(f'\033[33m-=-\033[m'*19)

num = int(input('Em qual número estou pensando? '))
sorte = randint(0, 10)
cs = 1

while sorte != num:
    if num < sorte:
        print('\033[31mMais... Tente mais um vez.\033[m')

    elif num > sorte:
        print('\033[31mMenos... Tente mais um vez.\033[m')

    num = int(input('Em qual número estou pensando? '))
    cs = cs + 1
    
print(f'\033[32mParabéns, você conseguiu acertar!!\033[m')
print(f'\033[32mE só precisou de {cs} tentativas para acertar o número\033[m')
#Finalizado com sucesso!
