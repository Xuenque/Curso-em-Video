#frase -> Pede uma frase para o usuario.
frase = input('Digite algo: ')

#type -> Mostra o tipo primitivo.
print(f'O tipo primitivo desse valor é: {type(frase)}')

#isspace -> Mostra se só tem espaços.
print(f'Só tem espaços? {frase.isspace()}')

#isnumeric -> Mostra se só é numerais.
print(f'É um numero? {frase.isnumeric()}')

#isalpha -> Mostra se é alfabético. (Se é formado apenas por letras)
print(f'É alfabético? {frase.isalpha()}')

#isalnum -> Mostra se tem letras e números.
print(f'É alfanumérico? {frase.isalnum()}')

#isupper -> Mostra se esta tudo em maiusculo.
print(f'Está em maiusculo? {frase.isupper()}')

#islower -> Mostra se esta tudo em minusculo
print(f'Está em minusculo? {frase.islower()}')

#istitle -> Mostra se esta capitalizado. (Se começa com as primeira letra da palavra em Maiusculo.)
print(f'Esta capitalizado? {frase.istitle()}')
