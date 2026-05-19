historico = []

ni = int(input('Digite um número: '))
c = int(input('Quer continuar?\nDigite 1 para "Sim" e 999 para "Não":\n'))
co = 1

while c != 999:
    nn = int(input('Digite o novo número: '))
    historico.append(nn)
    c = int(input('Quer continuar?\nDigite 555 para "Sim" e 999 para "Não":\n'))
    co += 1
print(f'Você digitou {co} números e a soma entre eles é {sum(historico)+ni}')
#Finalizado com sucesso!
