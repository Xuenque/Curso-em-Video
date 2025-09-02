salario = float(input('Qual é o salário do funcionário? R$ '))
if salario > 1250:
    print(f'Quem ganhava R$ {salario} passa a receber R$ {salario + (salario * 10 / 100):.2f}')
else:
    print(f'Quem ganhava R$ {salario} passa a receber R$ {salario + (salario * 15 / 100):.2f}')
#Finalizado com sucesso!