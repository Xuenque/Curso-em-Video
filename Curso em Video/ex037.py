numero = int(input('Digite um número: '))
escolha = int(input('Escolha uma das bases para conversão'
                    '\n1) Converter para BINARIO \n2) Converter para OCTAL \n3) Converter para HEXADECIMAL \nOpção: ') )
if escolha == 1:
    print(f'{numero} convertido para Binario é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    ler = int(input('Opção invalida'))
#Finalizado com sucesso!