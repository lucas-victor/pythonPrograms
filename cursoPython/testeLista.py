

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista2 = ['a', 'b', 'c', 'd', 'e']

carrinho = []
produto = ''


print(f'lista1 = {lista1}')
print(f'lista2 = {lista2}')

for item in lista2:
    print(item)

for item in lista1:
    lista2.append(item)

print(f'lista2 modificada: {lista2}')

lista3 = []
lista4 = []

print(f'lista2 modificada: {lista2}')

for item in lista2:
    if type(item) is not str:
        lista3.append(item)
        lista2.remove(item)
        print(f'item removido da lista 2: {item}')

    elif type(item) is not int:
        print(f'este item é um número: {item}')
        lista4.append(item)
    print(f'Item: {item} --  Tipo: {type(item)}')

print(f'lista1: {lista1}')
print(f'lista2: {lista2}')
print(f'lista3: {lista3}')
print(f'lista4: {lista4}')



