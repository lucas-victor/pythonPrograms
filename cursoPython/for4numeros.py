n1 = int(input(f'Digite o 1º número: '))
n2 = int(input(f'Digite o 2º número: '))
n3 = int(input(f'Digite o 3º número: '))
n4 = int(input(f'Digite o 4º número: '))

t = (n1, n2, n3, n4)

print(f'Voce digitou os valores {t}')

if 9 in t:
    print('tem o número: 9')
if 3 in t:
    print(f'tem o número 3 na posição: {t.index(3)}')
c = 0
for i in range(0, len(t)):
    if t[i] % 2 == 0:
        c += c
print(f'Os valores pares digitados foram: {c}')

