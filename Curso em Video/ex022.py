from time import sleep
nome = input('Digite o seu nome para analise simples: ').strip().title()
s = nome.split()
print(f'Analisando seu nome...')
sleep(1)
print(f'Seu nome em maiúsculas é {nome.upper()}'
      f'\nSeu nome em minúsculas é {nome.lower()}'
      f'\nSeu nome tem o total de {len(nome)-nome.count(' ')} letras'
      f'\nSeu primeiro nome é {s[0]} e tem {len(s[0])} letras')
#Finalizado com sucesso!