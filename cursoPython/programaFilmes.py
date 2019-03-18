#!/usr/bin/env python3
"""Programa para administrar uma lista com os filmes favoritos"""
import os
import sys

# Pega qual é o SO
so = sys.platform
so_clear = ''

# Defini o argumento para limpeza de tela de acordo com o SO
if (so == 'linux'):
    so_clear = 'clear'
elif (so[:3] == 'win'):
    so_clear = 'cls'

# Função lambda para limpeza de tela
if so_clear:
    limpar = lambda l: os.system(l)
else:
    limpar = lambda l: l

def main():
    """Inicializa o programa"""

    limpar(so_clear)
    print('Programa para administrar sua lista de filmes favoritos')
    print()

    while True:
        print()
        print('Escolha uma das opções abaixo\n')
        print('1 - Ver a lista')
        print('2 - Adicionar filmes na lista')
        print('3 - Excluir filmes da lista')
        print('0 - Sair\n')

        opcao = input('Entre com o número da opcao: ')
        print()

        if (opcao == '1'):
            ver()
        elif (opcao == '2'):
            adicionar()
        elif (opcao == '0'):
            sys.exit(0)
        else:
            print('Opcao inválida')
def existe():
    """Verifica se o arquivo filmes.txt existe"""
    if os.path.isfile('.tmp/filmes.txt'):
        return '.tmp/filmes.txt'
    else:
        return ''

def ver():
    """Mostra na tela do terminal 20 itens por vez da lista de filmes"""

    arq = existe()
    if not arq:
        input("O arquivo filmes.txt ainda não foi "
              "criado, tecle enter para continuar")
        return

    limpar(so_clear)
    print("Lista de Filmes:")
    print("(tecle enter para continuar)\n")
    with open(arq, 'r') as arquivo:
        filmes = arquivo.readlines()
        x = 0

        for filme in filmes:
            # Aqui declaramos end como um carcter vazio pois os
            # itens no arquivo já possuem um caracter de nova linha
            print(filme, end='')
            if x > 20:
                x = 0
                input()
            x += 1

def adicionar():
    """Adiciona filmes ao arquivo"""
    filmes = []
    opcao = 'a'
    arq = existe()

    if not arq:
        opcao = 'w'

    limpar(so_clear)
    print("Entre com os filmes digite 0 para sair")
    while True:
        filme = input()
        if filme != '0':
            filmes.append(filme)
        else:
            break

    with open(arq, opcao) as arquivo:
        for filme in filmes:
            # insere um caracter de nova linha até o penultimo item
            arquivo.write("{0}{1}".format(filme, '\n'))

        return

main()