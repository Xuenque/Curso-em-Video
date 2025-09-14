preco = float(input('Preço das compras: R$ '))
pagamento = int(input('FORMA DE PAGAMENTO. \n1 - á vista dinheiro/cheque \n2 - á vista cartão \n3 - 2x no cartão '
                      '\n4 - 3x ou mais no cartão \nOpção: '))

if pagamento == 1:
    print(f'O preço do produto de R$ {preco:.2f} a vista no dinheiro/cheque sai por R$ {preco - (preco * 10 / 100):.2f}')

elif pagamento == 2:
    print(f'O preço do produto de R$ {preco:.2f} a vista no cartão sai por R$ {preco - (preco * 5 / 100):.2f}')

elif pagamento == 3:
    print(f'O produto de R$ {preco:.2f} fica por 2x de R$ {preco / 2:.2f} \033[34mSEM JUROS\033[m no cartão')

elif pagamento == 4:
    vezes = int(input('Quantas vezes? \n'))
    if vezes < 3:
        print(f'O produto de R$ {preco:.2f} em 2x no cartão fica R$ {preco / vezes:.2f}')
    elif vezes >= 3:
        print(f'O preço do produto de R$ {preco:.2f} em {vezes}x de R$ {(preco + (preco * 20 / 100)) / vezes:.2f} \033[31mCOM JUROS\033[m no cartão sai por R$ {preco + (preco * 20 / 100):.2f}')
else:
    print('\033[31mOpção invalida\033[m')
#Finalizado com sucesso!
