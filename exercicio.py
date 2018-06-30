#!/usr/bin/python3
from pprint import pprint
frutas = [
    {'tipo':'banana', 'preco':5.4, 'quant':6},
    {'tipo':'pera', 'preco':8.3, 'quant':2}, 
    {'tipo':'abacaxi', 'preco':7.5, 'quant':10},
    {'tipo':'limao', 'preco':3.2, 'quant':5},
]

frutas1 = []
for fruta in frutas:
    fruta['preco'] += fruta['preco'] * 0.1
    frutas1.append(fruta)
pprint(frutas1)
