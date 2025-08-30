num = int(input('Digite um número: '))
print(f'Analisando o número {num}'
      f'\nUnidade: {num%10}'
      f'\nDezena: {(num//10)%10}'
      f'\nCentena: {(num//100)%10}'
      f'\nMilhar: {num//1000}')
#Finalizado com sucesso!