#outra forma de criar tuplas com range
#t2 = list(range(2, 10))
#print(t2)
#valores.sort()
#valores.sort(reverse=True)


#inicializar lista vazia, 2 formas:
listaVazia = []
listaVazia2 = list()

lista = [2, 3, 5, 9]
lista[2] = 4
lista.append(10)
lista.sort(reverse=True)
lista.insert(0, 11)
lista.pop() #remove valores. o último ou passado no parentese .pop(2)
lista.remove(2) #remove o primeiro valor 2 encontrado na lista de onde começou(esquerda pra direita).
print(lista)
print(f'Essa lista tem {len(lista)} itens')


