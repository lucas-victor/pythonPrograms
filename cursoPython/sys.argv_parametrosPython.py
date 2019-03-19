"""
sys

    argv - devolve os argumentos passados na linha de comando

Flags --> -l 14 = Define o número de linhas a ser lido por iteração.

"""

import sys

print(sys.argv)

def mais(texto, numLinhas=15):
    linhas = texto.splitlines()

    while linhas:
        chunk = linhas[:numLinhas]
        linhas = linhas[numLinhas:]
        for linha in chunk: print(linha)
        if linhas and input('mais?') not in ['s', 'S']: break

if __name__ == '__main__':
    arq, nLinhas = "", 15
    if len(sys.argv) > 1:
        mais(open(sys.argv[1]).read(), 5)
    if len(sys.argv) > 2:
        if '-l' in sys.argv:
            nLinhas = int(sys.argv[sys.argv.index('-l') + 1])
    mais(arq, nLinhas)

