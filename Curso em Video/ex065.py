maior = 0
menor = 0
soma = 0
c = 0
n = int(input('Digite um número: '))
r = str(input('Quer continuar? [S/N]\n')).upper()

soma += n
c += 1
maior = n
menor = n

while r != 'N':

    n = int(input('Digite mais um número: '))

    soma += n
    c += 1

    if n > maior:
        maior = n

    elif n < menor:
        menor = n

    r = str(input('Quer continuar? [S/N]\n')).upper()

media = soma / c
print(f'A média dos números digitados é {media}\nSendo o {maior} o maior valor e o {menor} o menor valor.')
#Finalizado com sucesso!
