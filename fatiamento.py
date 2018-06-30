#!/usr/bin/python3
nomes =  ['daniel', 'joao', 'maria', 'ana']
numeros = list(range(10))

copia = nomes[1:]
nomes[0] = 'pedro'
print(copia)
print(nomes)