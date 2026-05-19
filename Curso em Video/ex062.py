print('=' * 28)
print(' ' * 4, '10 TERMOS DE UM PA')
print('=' * 28)

pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

total = 10
contador = 1
mais_termos = 0.1
historico = []

while mais_termos != 0:
    while contador <= total:
        print(f'{pt}', end=' ')
        historico.append(pt)
        contador += 1
        pt += r
    mais_termos = int(input('\nDeseja mostrar mais quantos termos?\n'))
    total = total + mais_termos

print(f'Você viu o total de {contador-1} termos\nObrigado pela participação.'
      f'\nTermos vistos: {historico}')
#Finalizado com sucesso!
