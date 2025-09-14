from datetime import date
ma = 0
me = 0
for i in range(7):
    ano_nascimento = int(input(f'Em que ano a {i + 1}° pessoa nasceu? '))
    if date.today().year - ano_nascimento >= 18:
        ma += 1
    else:
        me += 1
print(f'Ao todo tivemos {ma} pessoas maiores de idade \nE também tivemos {me} pessoas menores de idade')
#Finalizado com sucesso!