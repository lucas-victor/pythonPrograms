
frase = '     Curso de Python     '
'''      0123456789....15     '''


print(' ===> frase.upper() ', frase.upper())
print(' ===> frase.lower() ', frase.lower())

'''Só primeira letra maiúscula'''
print(' ===> frase.capitalize()', frase.capitalize())

'''Primeira letra de cada palavra maiúscula.'''
print(' ===> frase.title() ', frase.title())

'''Troca palavra ou letras.'''
print(' ===> frase.replace("Python", "PHP")', frase.replace('Python', 'PHP'))

'''Tira espaços.'''
print(' ===> frase.strip() ', frase.strip())

'''corta espaço da direita'''
print(' ===> frase.rstrip() ', frase.rstrip())

'''Corta espaço da esquerda.'''
print(' ===> frase.lstrip() ', frase.lstrip())

#tamanho.
print(' ===> len(frase)', len(frase))

#localizar posição cortando de 0 a 13 posição..
print(' ===> frase.find("P"): ', frase.find('P'))

print(' ===> frase.count("o", 0, 10) ', frase.count('o', 0, 10))

#'''do início até a 10ª posição, Id=9.'''
print(' ===> frase[:10] ', frase[:10])

#tudo menos 5 últimas casas.
print(' ===> frase[:-5] ', frase[:-5])

#da casa 1 até a 15 de 2 em 2.
print(' ===> frase[1:15:2] ', frase[1:15:2])

#comeca no 6 até o fim de 2 em 2.
print(' ===> frase[6::2] ', frase[6::2])

#do 1 até 3. Lembrando que não pega casa 3.
print(' ===> frase[1:3] ', frase[1:3])

#quantas vezes tem (o) minusculo na frase comçando da posição 0 indo até a 5.
print(' ===> frase.count("o", 0, 5) ', frase.count('o', 0, 5))



