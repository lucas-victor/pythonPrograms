
while True:
    r = int(input('Digite qual número deseja ver a tabuada (ou numero negativo para parar): '))
    if r < 0:
        #styles 0, 1, 4, 7
        #text 30 a 37
        #background 40 a 47
        #Ex: \033[0;31;40
        print('\033[7;30mPROGRAMA TABUADA ENCERRADO! Volte sempre!\033[m')
        break
    print('----------------------------------------------------------------')
    print(f'################## A tabuada do número {r} é: ##################')

    for i in range(1,11):
        n1 = r * i
        print(f'{r} x {i} = {n1}')

    print('----------------------------------------------------------------')
