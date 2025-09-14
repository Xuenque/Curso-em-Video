soma = 0
qtd = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        qtd += 1
print(f'\nA soma de todos os {qtd} valores solicitados é {soma}')
#Finalizado com sucesso!