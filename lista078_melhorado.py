#exercicio78
#faça um programa que leia 5 valores numericos
#e guarde-os em uma lista.
#no final,mostre qual foi o maior e o menor 
#valor digitado e suas repctivas posiçoes na lista

lista_numeros = [int(input("digite um numero")) for _ in range(5)]

#criando as variaveis do maior e do menor valor

menor_valor_da_lista = min(lista_numeros)
maior_valor_da_lista = max(lista_numeros)

#criando uma lista pegando os indices dos numeros que sejam de valor igual ao maior e menor valor(pq pode ter mais de um)

indices_dos_menores_valores =[indice for indice, valor in enumerate(lista_numeros) if valor == menor_valor_da_lista] 
indices_dos_maiores_valores = [indice for indice, valor in enumerate(lista_numeros) if valor == maior_valor_da_lista]

#criando o print do maior e menor valor e a posiçao dos indices onde eles apareceram

print(f"o menor valor é {menor_valor_da_lista} e ele apareceu nas posiçoes {indices_dos_menores_valores}")

print(f"o maior valor é {maior_valor_da_lista} e ele apareceu nas posiçoes {indices_dos_maiores_valores}")


