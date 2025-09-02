s1 = float(input('Primeiro Segmento: '))
s2 = float(input('Segundo Segmento: '))
s3 = float(input('Terceiro Segmento: '))
if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    print('\033[32mOs segmentos PODEM FORMAR um triângulo!\033[m')
else:
    print('\033[31mOs segmentos NÃO PODEM FORMAR um triângulo!\033[m')
#Finalizado com sucesso!