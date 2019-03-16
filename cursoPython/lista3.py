#lista = []
lista = list()

while True:
    num = int(input('Digite um número: '))

    if num not in lista:
        lista.append(num)

    cnt = input('Quer continuar? [s/n]').lower()
    if cnt == 'n':
        soma = 0
        for i in range(0, len(lista)):
            soma += lista[i]
        media = soma/len(lista)
        lista.sort()
        print(f'Os números digitados em ordem crescente são: {lista}')
        print(f'A media dos números digitados é: {media}')
        break

