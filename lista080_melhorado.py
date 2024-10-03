#crie um programa onde o usuario possa digitar cinco valores
#numericos e cadastra-los em uma lista,ja na posição correta
#de inserção(sem usar o sort()). no final, mostre a lista
#ordenada na tela.

lista = []

for _ in range(5):
    numero = int(input("digite um numero inteiro"))

    if len(lista)==0:
        lista.append(numero)

    else:
        posicao = 0

        while posicao<len(lista) and lista[posicao] < numero:
            posicao+=1
        lista.insert(posicao,numero)

print(f"lista em ordem crescente é {lista}")





