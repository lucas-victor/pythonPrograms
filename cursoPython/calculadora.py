def somar(x, y):
    soma = x + y
    return soma

def multiplicar(x, y):
    mult = x * y
    return mult

def dividir(x, y):
    div = x / y
    return div

def subtrair(x, y):
    sub = x - y
    return sub

def exibeMenu():
    print('=' * 20)
    print(' ' * 4, 'CALCULADORA', ' ' * 5)
    print('=' * 20)
    print('1 = SOMAR\n'
          '2 = SUBTRAIR\n'
          '3 = DIVIDIR\n'
          '4 = MULTIPLICAR')
    print('=' * 20)

def continuar():
    while True:
        continua = str(input('Deseja continuar? (s/n)').lower())
        if continua == 's' or continua == 'n':
            break
        else:
            print('Digite um valor válido.')
    return continua

while True:
    exibeMenu()
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    oper = int(input('Digite a operação desejada: '))

    if oper == 1:
        resultado = somar(num1, num2)
        input(f'O valor da soma foi: {resultado}\nTecle enter para continuar')
        if continuar() == 's':
            continue
        else:
            break
    elif oper == 2:
        resultado = subtrair(num1, num2)
        input(f'O valor da subtração foi: {resultado}\nTecle enter para continuar')
        if continuar() == 's':
            continue
        else:
            break
    elif oper == 3:
        resultado = dividir(num1, num2)

        input(f'O valor da divisão foi: {resultado}\nTecle enter para continuar')
        if continuar() == 's':
            continue
        else:
            break
    elif oper == 4:
        resultado = multiplicar(num1, num2)
        input(f'O valor da multiplicação foi: {resultado}\nTecle enter para continuar')
        if continuar() == 's':
            continue
        else:
            break
    else:
        print('Digite um valor válido para operação')
        if continuar() == 's':
            continue
        else:
            break

