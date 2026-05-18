from random import randint

print(f'\033[33m-=-\033[m'*19)
print('\033[35mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print(f'\033[33m-=-\033[m'*19)


num = int(input('Em qual número estou pensando? '))
sorte = randint(0, 5)
cs = 1
while sorte != num:

    print('\033[31mNão foi dessa vez, mais sorte na próxima.\033[m')

    num = int(input('Em qual número estou pensando? '))
    cs = cs + 1

print(f'\033[32mParabéns, você conseguiu acertar!!\033[m')
print(f'\033[32mE só precisou de {cs} para acertar o número\033[m')
#Finalizado com sucesso!
