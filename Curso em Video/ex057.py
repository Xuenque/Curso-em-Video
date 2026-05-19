sexo = ''
while sexo not in ['F', 'M']:
    sexo = str(input('Qual o seu sexo? [F/M] ')).upper()
    
    if sexo not in ['F', 'M']:
        print('Opção invalida, digite novamente')
        
print('Opção aceita, obrigado por participar da nossa pesquisa')
#Finalizado com sucesso!
