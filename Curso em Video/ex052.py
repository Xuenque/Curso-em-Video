num = int(input('Digite um número: ')
for i in range(num):
    if num % i == 0:
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')

#Em contrução...
