qt = int(input('Quantos termos desejas ver? \n'))

t1 = 0
t2 = 1
ct = 3

if qt == 0:
    print('Ficamos por aqui então.')

elif qt == 1:
    print(f'{t1}')

else:
    print(f'{t1} -> {t2}', end=' ')

    while ct <= qt:
        t3 = (t1 + t2)
        print(f'-> {t3}', end=' ')
        t1 = t2
        t2 = t3
        ct += 1
#Finalizado com sucesso!
