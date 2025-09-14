cont = 0
num = int(input('Digite um número: '))
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[33m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print(i, end='')
print('')
if cont == 2:
    print(f'\n\033[mO número {num} foi divisível {cont} vezes \nE por isso ele É PRIMO!')
else:
    print(f'\n\033[mO número {num} foi divisível {cont} vezes \nE por isso ele NÃO É PRIMO!')
#Finalizado com sucesso!