def calculadora():
    while True:
        print('Opções: ')
        print('Digite "somar" para efetuar uma soma: ')
        print('Digite "subtrair" para efetuar uma subtração: ')
        print('Digite "multiplicar" para efetuar uma multiplicação: ')
        print('Digite "dividir" para efetuar uma divisão: ')
        print('Digite "sair" para deixar o programa: ')
        user_input = input(': ')
        if(user_input == 'sair'):
            break
        elif(user_input == 'somar'):
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            print('A resposta é {}'.format(n1 + n2))
        elif(user_input == 'subtrair'):
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            print('A resposta é {}'.format(n1 - n2))
        elif(user_input == 'multiplicar'):
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            print('A resposta é {}'.format(n1 * n2))
        elif(user_input == 'dividir'):
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
            print('A resposta é {}'.format(n1 / n2))
        else:
            print('Entrada inválida!')

calculadora()
