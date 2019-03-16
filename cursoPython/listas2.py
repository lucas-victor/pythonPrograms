a = [2, 3, 5, 7]
# assim se cria ligação entre as listas, se alterar uma altera a outra. Tipo um ponteiro.
b = a
#Assim se faz a cópia de uma lista inteira
c = a[:]
print(a)
print(b)
b[2] = 10
#note que o valor da lista a e o valor da lista b são alterados devido a atribuição acima.
print(a)
print(b)
print(c)
valores = list()

for cont in range(1, 5):
    valores.append(int(input(f'Digite o {cont}º valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')

