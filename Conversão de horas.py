from datetime import datetime


def converteHora(hora, minutos):
    if 24 >= hora > 12 and 0 <= minutos < 60:
        horaconvertida = str(hora - 12) + ':' + str(minutos) + ' P.M'
    elif 0 < hora < 13 and 0 <= minutos < 60:
        horaconvertida = str(hora) + ':' + str(minutos) + ' A.M'
    else:
        print('Hora/minutos inválidos!')
    return str(horaconvertida)


while True:
    hora = int(input('Digite a hora a ser convertida: '))
    minutos = int(input('Digite os minutos: '))
    print(converteHora(hora, minutos))
    cont = input('Digite \'sair\' para terminar o programa: ')
    if cont == 'sair':
        break
    else:
        print('Executando novamente . . .')
        continue

