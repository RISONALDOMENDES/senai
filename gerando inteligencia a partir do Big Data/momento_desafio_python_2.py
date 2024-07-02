# -*- coding: utf-8 -*-
"""
Resposta ao Momento Desafio 2 de programação em Python.

Lembre-se: não existe uma única resposta para os desafios.
Considere o resultado do código abaixo e veja se ele se aproxima do que você conseguiu com o seu.

"""

"Criando o dicionário A"

A = {'Cor1':'Azul', 'Cor2':'Vermelho','Cor3':'Verde','Cor4':'Cinza','Cor5':'Laranja'}

"Criando uma lista B contendo as chaves do dicionário A"

B = list(A.keys())

"Pegando o input numérico do usuário"
C = input("Digite um número entre 1 e 5: ")

print("Você escolheu o número " + C + ". No dicionário ele corresponde ao elemento: " + A[B[int(C) - 1]])