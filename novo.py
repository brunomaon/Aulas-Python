#!/usr/bin/python3
nomes = ['daniel', 'joao', 'pedro', 'maria']

nomes= [nome.title() for nome in nomes]
print(nomes)

exit()


nomes = ['daniel', 'joao', 'pedro', 'maria']

for nome in nomes:
    if nome == 'adamastor':
        print('achei')
        break
else:
    print('nao achei')