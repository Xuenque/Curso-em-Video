historico = []
co = 0
print('Digite 999 quando quiser para o programa!')
ni = int(input('Digite um número: '))
while ni != 999:
    historico.append(ni)
    ni = int(input('Digite um número: '))
    co += 1
print(f'Você digitou {co} números e a soma entre eles é {sum(historico)}')
#Finalizado com sucesso!
