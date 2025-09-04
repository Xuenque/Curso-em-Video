n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

if (n1 + n2) / 2 < 5:
    print(f'Com as notas {n1} e {n2}, a média do aluno é {(n1 + n2) / 2:.1f}'
          f'\nO aluno esta \033[31mREPROVADO\033[m.')

elif (n1 + n2) / 2 >= 5 and (n1 + n2) / 2 < 6.9:
    print(f'Com as notas {n1} e {n2}, a média do aluno é {(n1 + n2) / 2:.1f}'
          f'\nO aluno esta de \033[33mRECUPERAÇÃO\033[m.')

elif (n1 + n2) / 2 >= 7:
    print(f'Com as notas {n1} e {n2}, a média do aluno é {(n1 + n2) / 2:.1f}'
          f'\nO aluno esta \033[32mAPROVADO\033[m.')
#Finalizado com sucesso!