t = ('WarCraft', 'Dota', 'Dota2', 'CS',
     'GodOfWar', 'Zelda', 'Mario', 'FinalFantasy7',
     'FinalFantasy8', 'FinalFantasy9', 'ChronoCross',
     'LegendOfDragon', 'MuOnline', 'Ragnarok')
#outra forma de criar tuplas com range
#t2 = list(range(2, 10))
#print(t2)

while True:

    print(t)
    print('')
    print('1 - Os cinco primeiros jogos:')
    print('2 - Os cinco últimos jogos:')
    print('3 - uma lista com os jogos em ordem alfabética:')
    print('4 - Saber a posição em que se encontra o jogo:')

    n = int(input('Selecione a opção através do número: '))

    if n == 1:
        for i in range(0, 5):
            print(t[i])
        r = input('Quer continuar? [S/N] ').upper()
        if r != 'S':
            break

    if n == 2:
        for i in range(len(t)-1, 8, -1):
            print(t[i])
        r = input('Quer continuar? [S/N] ').upper()
        if r != 'S':
            break

    if n == 3:
        ord = sorted(t)
        for o in ord:
            print(o)
        r = input('Quer continuar? [S/N] ').upper()
        if r != 'S':
            break

    if n == 4:
        r = input('Digite um nome de jogo para saber a posição: ')
        for pos, nome in enumerate(t):
            #print(pos, nome)
            if nome == r:
                print(t.index(nome))
        r2 = input('Quer continuar? [S/N] ').upper()
        if r2 != 'S':
            break
