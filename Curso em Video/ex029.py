vel = int(input('Qual a velocidade do seu carro? '))
if vel < 80:
    print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
else:
    print(f'\033[31mMultado! Você excedeu o limite permitido que é de 80km/h'
          f'\nVocê deve pagar uma multa de R$ {(vel-80)*7.00:.2f}\033[m')
#Finalizado com sucesso!