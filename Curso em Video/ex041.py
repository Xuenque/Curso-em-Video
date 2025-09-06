from datetime import date

ano = int(input('Ano de nascimento: '))

print(f'O atleta tem {date.today().year - ano} anos')

if date.today().year - ano <= 9:
    print('Classificação: MIRIM')

elif 9 < date.today().year - ano <= 14:
    print('Classificação: INFANTIL')

elif 14 < date.today().year - ano <= 19:
    print('Classificação: JUNIOR')

elif 19 < date.today().year - ano <= 25:
    print('Classificação: SÊNIOR')

elif date.today().year - ano > 25:
    print('Classificação: MASTER')
#Finalizado com sucesso!