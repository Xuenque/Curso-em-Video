frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso =''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

print(f'O inverso de {frase} é {inverso}')
if inverso == junto:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
#Finalizado com sucesso! Não entendi ainda pq do for pra isso, da pra fazer muito mais simples sem, mas ta ai kk