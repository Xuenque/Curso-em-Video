num = int(input('Digite o seu número: '))
fatorial = 1
while num > 0:
    fatorial = fatorial * num
    num -= 1
    if num > 0:
        print(f'{num + 1} x ', end='')
    else:
        print(f'{num + 1} = ', end='')
print(f'{fatorial}')
#Finalizado com sucesso!
