pessoas = {'nome': 'Lucas Victor', 'sexo': 'M', 'idade': 32}

for k, v in pessoas.items():
    print(k.upper(), end=': ')
    print(v)

for k in pessoas.keys():
    print('Chave:', k, end=' ')
print('')
for v in pessoas.values():
    print('Valor:', v, end=' ')

print('')

print(pessoas)
#apagar item no dicionario
del pessoas['idade']
print(pessoas)
#inserir item no dicionario
pessoas['formacao'] = 'superior incompleto'
print(pessoas)

#print('Exibindo a copia de pessoas: ')
#print(copiapessoas)


