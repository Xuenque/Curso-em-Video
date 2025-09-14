print('=' * 28)
print(' ' * 4, '10 TERMOS DE UM PA')
print('=' * 28)

pt = int(input('Primeiro Termo: '))
r= int(input('Razão: '))
decimo = pt + (10 - 1) * r
for i in range(pt, decimo + r, r):
    print(i,end=' -> ')
print('ACABOU')
#Finalizado com sucesso!