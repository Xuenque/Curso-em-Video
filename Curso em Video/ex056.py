from time import sleep

idades = []
maior_idade = 0
homem_velho = ''
mulher_20 = 0

for i in range(4):
    print(f'-' *5,f'{i + 1}° Pessoa', '-' * 5)
    nome = str(input('Nome: ')).strip(). title()
    idade = int(input('Idade: '))
    idades.append(idade)
    sexo = str(input('Sexo [M/F]: ')).strip()

    if i == 0 and sexo in 'Mm':
        maior_idade = idade
        homem_velho = nome
    
    if sexo in 'Mm' and idade > maior_idade:
        maior_idade = idade
        homem_velho = nome
    
    if sexo in 'Ff' and idade > 20:
        mulher_20 += 1

print('\nAnalisando...')
sleep(1)
print(f'A média de idade do grupo é de {(sum(idades)/4)} anos')
print(f'O mais velho tem {maior_idade} anos e se chama {homem_velho}')
print(f'Ao todo são {mulher_20} mulher com menos de 20 anos')
#Finalizado com sucesso!