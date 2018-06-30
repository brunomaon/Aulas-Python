#!/usr/bin/python3
# bem vindo
nome = input("Nome do aluno:  ")
nome = nome.title()

soma = 0
for x in range(3):
    nota = int(input("Digite nota {}: ".format(x+1)))
    soma += nota

media = soma/3

if  media >= 7:
    result = 'aprovado'
else:
    result = 'reprovado'

print("O aluno {0} foi {1} com media {2}".format(nome.title(), result, media))
