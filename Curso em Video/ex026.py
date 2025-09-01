frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count('A')} vezes na frase.'
      f'\nA primeira letra "A" apareceu na posição {frase.find('A')+1}'
      f'\nA útima letra "A" apareceu na posição {frase.rfind('A')+1}')
#Finalizado com sucesso!