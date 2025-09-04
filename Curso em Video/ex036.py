valor_casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos_financiamento = int(input('Quantos anos de financiamento? '))
prestacao = valor_casa / (anos_financiamento * 12)

if prestacao > salario * 30 / 100:
    print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento} a prestação será de R$ {prestacao:.2f}'
          f'\nEmprestimo \033[31mNEGADO\033[m')
else:
    print(f'Para pagar uma casa de R$ {valor_casa:.2f} em {anos_financiamento} a prestação será de R$ {prestacao:.2f}'
          f'\nEmprestimo \033[32mCONCEDIDO\033[m')
#Finalizado com sucesso!