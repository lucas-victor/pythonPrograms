"""

    Argumentos no python

    flags também.

"""

import sys

print(sys.argv)

if len(sys.argv) > 1:
    print(f'O número de parâmetros é maior que 1. Valor do parametro 2 é: {sys.argv[2]}')
elif len(sys.argv) > 2:
    print(f'Foram passado mais de 2 parametros para o programa, são eles 1 {sys.argv[2]} e 2 {sys.argv[3]}')
else:
    input('não foi passado nenhum parâmetro para o programa. \n Tecle enter para sair.')