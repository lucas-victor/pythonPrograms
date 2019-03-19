import os

os.system("ls -lathr")

os.system('echo "Foi exibido o comando ls -lathr..........................."')

#guarda o exit code do comando. --0 sucesso  -- !=0 erro --por exemplo 1
var = os.system('ls')
print(var)

#guarda a saída do comando executado no terminal
var = os.pytho