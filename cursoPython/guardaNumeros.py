c = 0
soma = 0
while True:
    n = int(input('Digite um número de 0 a 1000: '))
    soma += n
    c += 1
    if c == 3:
        media = soma / c
        print(f'Você digitou o número correto em {c} tentativas')
        print(f'A soma dos números foi: {soma}')
        print(f'A media dos valores foi: {media}')
        break
