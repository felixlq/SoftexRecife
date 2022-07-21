def cabecario(msg):
    print('=-' * 30)
    print('{:^60}'.format(msg))
    print('=-' * 30)


def calculadora(a, b, c):
    if c == 1:
        s = a + b
        print(s)
    elif c == 2:
        s = a - b
        print(s)
    elif c == 3:
        s = a * b
        print(s)
    elif c == 4:
        s = a / b
        print(s)
    else:
        c >= 5
        print('\033[1;31m Selecione uma opção válida! \033[m')



cabecario('CALCULADORA COM FUNÇÃO')

num1 = float(input('Indique o primeiro número: '))
num2 = float(input('Indique o segundo número: '))
op = int(input('selecione o operador:\n[1 para soma]\n[2 para subtração]\n[3 para multiplicação]\n[4 para divisão]\n>>>> '))

calculadora(num1, num2, op)






