#!/usr/bin/python3

nomes = []
while True:
    nome = input("Digite um nome: ")

    if nome.lower().strip() == 'sair':
        break
    nomes.append(nome)

# print(nomes[0])
for pessoa in nomes:
    if pessoa.lower().strip() == 'ana':
        print('achei!')
        break
else:
    print('nao achei a ana')