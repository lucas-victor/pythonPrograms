estado = dict()
brasil = list()

for count in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('sigla do estado: '))
    #lembrar que para dicionarios é necessario utilizar o copy.
    brasil.append(estado.copy())

#for pra lista
for e in brasil:
    #for pro dicionario dentro do item(e) da lista.
    for k, v in e.items():
        print(f'A chave é: {k} O valor é: {v}')

#for para exibir os valores de cada (estado) de cada item da lista (brasil).
for e in brasil:
    for v in e.values():
        print(f'O segundo for tem os valores: {v}')

#for para exibir as chaves do dicionario (estado) de cada item da lista (brasil).
for e in brasil:
    for k in e.keys():
        print(f'As chaves exibidas no 3 for são: {k}')