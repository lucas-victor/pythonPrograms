'''

Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média

'''


pessoas = dict()
listaPessoas = list()
listaMulheres = list()
listaAcimaMedia = list()

resp = 'S'
cont = 0
somaIdade = 0

while resp == 'S':
    cont += 1
    pessoas['nome'] = str(input('Digite o nome: '))

    while True:
        pessoas['sexo'] = str(input('Digite o sexo, [m/f]: ')).upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO: digite o valor correto M ou F.')

    pessoas['idade'] = int(input('Digite a idade: '))
    #adiciona pessoas na lista
    listaPessoas.append(pessoas.copy())

    #se mulher coloca na lista de mulheres
    if pessoas['sexo'] == 'F':
        listaMulheres.append(pessoas.copy())
    somaIdade += pessoas['idade']
    while True:
        resp = str(input('Você deseja continuar? [s/n]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO: digite um valor valido: [s/n]: ')

print(f'A quantidade de pessoas cadastradas é: {cont}')
print(f'A lista de mulheres é: {listaMulheres}')



#exibe todos os dados de cada mulher
c = 0
for i in listaPessoas:
    c += 1
    for k, v in i.items():
        print(f'Mulher {c}: {k} e {v}', end=' ')

#media idade
media = somaIdade/cont
print(f'A media de idades é: {media}')
print(f'A lista de pessoas cima da media de idade que é {media} é:')

#exibe lista de acima da media de idade.
for i1 in listaPessoas:
    for k, v in i1.items():
        if k == 'idade':
            if v > media:
                print(f'Está acima da media de idade: {i1}')



print('A lista de pessoas é: ')
print(listaPessoas)





