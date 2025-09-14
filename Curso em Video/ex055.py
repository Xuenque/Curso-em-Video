maior = 0
menor = 0

for i in range(5):
    peso = float(input(f'Peso da {i + 1}° pessoa (kg): '))

    if i == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é de {maior} \nO menor peso é de {menor}')
#Finalizado com sucesso!