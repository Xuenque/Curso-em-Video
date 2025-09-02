distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    print(f'Você esta prestes a começar uma viagem de {distancia}Km.'
          f'\nE o preço da sua passagem será de  {distancia*0.50:.2f}')
else:
    print(f'Você esta prestes a começar uma viagem de {distancia}Km.'
          f'\nE o preço da sua passagem será de R$ {distancia*0.45:.2f}')
#Finalizado com sucesso!