import random
c = 0
while True:
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print('=-= VAMOS JOGAR PAR OU ÍMPAR? =-=')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    c = c + 1

    n = int(input('Diga um valor: '))
    rand = random.randint(1,10)
    soma = n + rand
    pi = str(input('PAR ou ÍMPAR? [P/I]').upper())

    if soma % 2 == 0 and pi == 'P':
        print(f'O número é PAR {soma}! Você jogou {n} e o PC jogou {rand}')
        print(f'Continue assim, você ganhou {c} vez(es) consecutivas! \n')
    elif soma % 2 != 0 and pi == 'I':
        print(f'O número é ÍMPAR {soma}! Você jogou {n} e o PC jogou {rand}')
        print(f'Continue assim, você ganhou {c} vez(es) consecutivas! \n')
    else:
        if soma % 2 == 0:
            print(f'GAME OVER. O PC ganhou, o número é PAR! {soma}')
            print('Tente novamente!')
            break
        else:
            print(f'GAME OVER. O PC ganhou, o número é ÍMPAR! {soma}')
            print('Tente novamente!')
            break

