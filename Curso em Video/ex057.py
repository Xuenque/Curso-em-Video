sexo = ''
while sexo not in ['F', 'M']:
    sexo = str(input('Iforme seu sexo: [F/M] ')).strip().upper()[0]
    
    if sexo not in ['F', 'M']:
        print('Opção invalida, digite novamente')
        
print('Opção aceita, obrigado por participar da nossa pesquisa')
#Finalizado com sucesso!
