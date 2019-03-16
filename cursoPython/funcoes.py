def somar(a, b, c):
    s = a + b + c
    return s

def cabecalho(msg):
    print('-' *30)
    print('-' *3, msg, '-' *4)
    print('-' *30)

r = somar(7, 5, 3)

cabecalho('CABEÇALHO DO PROGRAMA')
print(f'a soma é {r}')