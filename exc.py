#!/usr/bin/python3
# Faça um programa que leia 20 números inteiros
# e armazene-os num vetor. Armazene os números 
# pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores.

par = []
impar = []
todos = []

for x in range (10):
    num = int(input('Digite o numero: '))
    todos.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(par)
print(impar)
print(todos)