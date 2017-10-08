# tabela de preços
print('Código       Nome        R$(Kg)')
print('101          Tomate      1,00')
print('102          Batata      1,20')
print('103          Abóbora     0,65')
print('104          Cenoura     1,65')
print('105          Cebola      0,90')


def preco(prod, qtd):
    if prod == 101:
        p = 1.00 * qtd
        return p
    elif prod == 102:
        p = 1.20 * qtd

    elif prod == 103:
        p = 0.65 * qtd

    elif prod == 104:
        p = 1.65 * qtd

    elif prod == 105:
        p = 0.90 * qtd

    return p


try:
    pdt = []
    subtotal = []
    total = 0
    x = 0
    while True:
        cod = int(input('Informe o código do produto: '))
        # pdt += [cod]
        pdt.append(cod)
        while cod > 105 or cod < 101:
            cod = int(input('Informe o código do produto: '))
            pdt.append(cod)
        qtd = int(input('Informe a quantidade em quilos: '))
        while qtd <= 0:
            qtd = int(input('Informe a quantidade em quilos: '))
            m = preco(cod, qtd)
        m = preco(cod, qtd)
        subtotal.append(qtd)
        if cod == 101:
            total += m

        elif cod == 102:
            total += m

        elif cod == 103:
            total += m

        elif cod == 104:
            total += m

        elif cod == 105:
            total += m

        c = int(input('Digite "1" para continuar comprando: '))
        if c == 1:
            continue
        else:
            print('- COMPRA FINALIZADA -')
            print('Produtos comprados: {}'.format(pdt, sep=", "))
            print('Quantidade respectiva(kg): {}'.format(subtotal, sep=", "))
            print('Total da compra: R$ {:.2f}'.format(total))
            break


except IndentationError:
    print('Problema de lógica..')
