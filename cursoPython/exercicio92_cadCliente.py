from datetime import datetime

def calculaAposentadoria(contr, idade):
    alvo = ((contr + 35) - datetime.now().year)
    aposentadoria = idade + alvo
    return aposentadoria

clientes = dict()

# le nomes
clientes['nome'] = str(input('Digite o nome: '))
clientes['nasc'] = int(input('Digite seu ano de nascimento: '))
clientes['idade'] = int(input('Digite sua idade: '))
#clientes['ctps'] = int(input('Tem carteira de trabalho? (digite 0(zero) se não) '))

#variavel decisao se tem carteira ctps.
ctps = int(input('Tem carteira de trabalho? (digite 0(zero) se não) '))

if ctps != 0:
    clientes['contratacao'] = int(input('digite o ano de contratacao: '))
    clientes['salario'] = float(input('Digite o seu salário: '))

    #usa função pra calcular aposentadoria
    clientes['aposentadoria'] = calculaAposentadoria(clientes['contratacao'], clientes['idade'])

    print('alvo da aposentadoria', clientes['aposentadoria'])
    print(clientes['aposentadoria'])

for k, v in clientes.items():
    print(f'O {k} é {v}: ')



