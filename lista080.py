#crie um programa onde o usuario possa digitar cinco valores
#numericos e cadastra-los em uma lista,ja na posição correta
#de inserção(sem usar o sort()). no final, mostre a lista
#ordenada na tela.

lista = []
valor0 = lista[0]
valor1 = lista[1]
valor2 = lista[2]
valor3 = lista[3]
valor4 = lista[4]

for i in range (5):
    numero= int(input("digite um numero inteiro: "))
    if len(lista) == 0:
        lista.insert(0,numero)
    
    elif len(lista)== 1 and numero> valor0: #sera que eu poderia comparar o direto numero > lista[0]?
        lista.insert(1,numero)

    elif len(lista)== 1 and numero< valor0: #sera que isso poderia ser um else dentro do elif de cima?
        lista.insert(0,numero)

    elif len(lista)== 2 and numero == min(lista):
        lista.insert(0,numero)
    elif len(lista)== 2 and numero == max(lista):
        lista.insert(2,numero)
    elif len(lista)== 2 and numero > valor0 and numero< valor1:
        lista.insert(1,numero)           


#codigo ruim va para o refeito no lista080_melhorado.py






