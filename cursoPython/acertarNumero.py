n = 1
b = 2
while True:

    n = int(input('Digite um número: '))

    if n == 1000:
        print('voce digitou o número 1000')
        r = str(input('Quer digitar outro número? [S/N]').upper())
        if r == 'S':
            print('Continuando...')
        else:
            print('Parando!')
            break
    elif n == 999:
        print('voce digitou o número 999')
        for c in range(0,3):
            r = str(input('Digite [N] 3 vezes para não continuar, ou continue apertando [S] 1 vez.').upper())
            if r == 'S':
                continue
            elif c == 3 and r == 'N':
                break
    elif n == 888:
        print('voce digitou o número 888')
        r = str(input('Digite qualquer número para continuar ou [N] para parar: '))
        if r == 'N':
            break
        else:
            b = 0
    elif n == 777:
        print('Você digitou o número 777')
        break
    else:
        print('Você não digitou o número corretamente!')




