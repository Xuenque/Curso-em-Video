from random import shuffle
a1 = input('Primeiro aluno: ').strip().title()
a2 = input('Segundo aluno: ').strip().title()
a3 = input('Terceiro aluno: ').strip().title()
a4 = input('Quarto aluno: ').strip().title()
lista_alunos = [a1,a2,a3,a4]
shuffle(lista_alunos)
print(f'A orde das apresentações vai ser {lista_alunos}')
#Finalizado com sucesso!