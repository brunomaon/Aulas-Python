#!/usr/bin/python3
# bem vindo
nome = input("Nome do aluno:  ")
nome = nome.title()
nota1 = int(input("Nota da primeira prova: "))
nota2 = int(input("Nota da segunda prova: "))
media = ((nota1 + nota2)/2)
print("O aluno {0} tem a media {1}".format(nome, media))

