from datetime import date
sexo = int(input('Qual o seu sexo? \n1 - Masculino \n2 - Feminino \nOpção: '))

if sexo == 1:
    ano = int(input('Ano de nascimento: '))

    #Idade Certa
    if date.today().year - ano == 18:
        print(f'Quem nasceu em {ano} tem {date.today().year - ano} anos em {date.today().year}'
            f'\nVocê deve se alistar IMEDIATAMENTE.')

    #Um ano a mais
    elif date.today().year - ano == 19:
        print(f'Quem nasceu em {ano} tem {date.today().year - ano} anos em {date.today().year}'
            f'\nvocê já deveria ter se alistado há {(date.today().year - ano) - 18} ano.'
            f'\nSeu alistamento deveria ter sido feito em {ano + 18}')

    #Passou da idade
    elif date.today().year - ano > 18:
        print(f'Quem nasceu em {ano} tem {date.today().year - ano} anos em {date.today().year}'
            f'\nvocê já deveria ter se alistado há {(date.today().year - ano) - 18} anos.'
            f'\nSeu alistamento deveria ter sido feito em {ano + 18}')

    #Um ano a menos
    elif date.today().year - ano == 17:
        print(f'Quem nasceu em {ano} tem {date.today().year - ano} anos em {date.today().year}'
              f'\nAinda falta {((date.today().year - ano) - 18) * -1} ano.'
              f'\nSeu alistamento devera ser feito em {ano + 18}.')

    #Menor de idade
    else:
        print(f'Quem nasceu em {ano} tem {date.today().year - ano} anos em {date.today().year}'
            f'\nAinda falta {((date.today().year - ano) - 18) * -1} anos.'
            f'\nSeu alistamento devera ser feito em {ano + 18}.')

elif sexo == 2:
    print('Você não precisa fazer alistamento. \nVá lavar uma louça.')

else:
    print('Opção invalida')
#Finalizado com sucesso!