print('=' * 28)
print(' ' * 4, '10 TERMOS DE UM PA')
print('=' * 28)

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 1

while cont < 11:
    print(f'{pt}', end=' -> ')
    pt += r
    cont += 1
print('Fim', end='')
#Finalizado com sucesso!
