peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

if peso / (altura * altura) < 18.5:
    print(f'O IMC da pessoa é {peso / (altura * altura):.1f}'
          f'\nVocê está \033[34mabaixo do aeso\033[m')

elif 18.5 < peso / (altura * altura) < 25:
    print(f'O IMC da pessoa é {peso / (altura * altura):.1f}'
          f'\nvocê está no \033[34mpeso ideal\033[m')

elif 25 < peso / (altura * altura) < 30:
    print(f'O IMC da pessoa é {peso / (altura * altura):.1f}'
          f'\nvocê está com \033[34msobrepeso\033[m')

elif 30 < peso / (altura * altura) < 40:
    print(f'O IMC da pessoa é {peso / (altura * altura):.1f}'
          f'\nvocê está com \033[34mobesidade\033[m')

else:
    print(f'O IMC da pessoa é {peso / (altura * altura):.1f}'
          f'\nvocê está com \033[34mobesidade mórbida\033[m')
