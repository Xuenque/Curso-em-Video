s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 + s2 > s3 and s1 + s3 > s2 and s2 + s3 > s1:
    if s1 == s2 == s3:
        print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo \033[34mEQUILÁTERO\033[m.')
    elif s1 == s2 != s3 or s1 == s3 != s2 or s2 == s3 != s1:
        print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo \033[34mISÓSCELES\033[m.')
    elif s1 != s2 != s3:
        print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo \033[34mESCALENO\033[m.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMA\033[m um triângulo.')
#Finalizado com sucesso!