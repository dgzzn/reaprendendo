print('='*10+' Tabuada '+'='*10)
n = int(input('Tabuada de: '))
for i in range(1,11):
    print('{} * {:2} = {:}'.format(n, i, n * i))