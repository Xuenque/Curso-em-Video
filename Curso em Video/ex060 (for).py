num = int(input('Digite o seu número: '))
fatorial = 1
for fato in range (num, 0, -1):
    fatorial = fatorial * fato
    if fato > 1:
        print(f'{fato}', end=' x ')
    else:
        print(f'{fato}', end=' = ')
print(f'{fatorial}')
#Finalizado com sucesso!
