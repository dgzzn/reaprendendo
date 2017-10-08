i = 0
maior = 0
while i < 5:
    x = int(input('Digite um número: '))
    if x > maior:
        maior = x
    i += 1
print(maior)