num1 = int(input('Digite o 1° valor: '))
num2 = int(input('Digite o 2° valor: '))
opcao = 0

while opcao != '5':
    print('Escolha uma das opções a baixo')
    opcao = str(input(f'[1]Somar \n[2]Muliplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa \nOpção: '))
    
    if opcao == '1':
        print(f'A soma entre os números {num1} e {num2} é igual a {num1 + num2}')
        
    elif opcao == '2':
        print(f'A multipliocação entre os números {num1} e {num2} é igual a {num1 * num2}')
        
    elif opcao == '3':
        if num1 > num2:
            print(f'O maior número entre {num1} e {num2} é o {num1}')
            
        else:
            print(f'O maior número entre {num1} e {num2} é o {num2}')
            
    elif opcao == '4':
        print('Digite os novos números')
        num1 = int(input('Digite o 1° valor: '))
        num2 = int(input('Digite o 2° valor: '))
        
    elif opcao not in ['1', '2', '3', '4', '5']:
        print('\033[31mOpção invalida, digite novamente.\033[m')
        
print('Obrigado pela participação \nPrograma encerrado!')
# Finalizado com sucesso!
