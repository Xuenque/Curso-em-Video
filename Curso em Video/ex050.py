soma = 0
cont = 0
for i in range(6):
    nums = int(input(f'Digite o {i + 1}° número: '))
    if nums % 2 == 0:
        soma += nums
        cont += 1
if cont == 1:
    print(f'Você informou {cont} número PAR, sendo o número {soma}')
elif cont == 0:
    print(f'Você não digitou nenhum número PAR')
else:
    print(f'Você informou {cont} números PARES, e a soma dos números é igual a {soma}')
# Finalizado e Melhorado com sucesso!