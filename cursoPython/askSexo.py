c = True
r = 'a'
while c == True:
    r = str(input('Digite o seu sexo: [M/F]')).upper()
    if r == 'M' or r == 'F':
        c = False
    else:
        print('Valores corretos são (M/F)')
print('O seu sexo é: {}'.format(r))


