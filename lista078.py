#exercicio78
#faça um programa que leia 5 valores numericos
#e guarde-os em uma lista.
#no final,mostre qual foi o maior e o menor 
#valor digitado e suas repctivas posiçoes na lista

lista_valores_numericos = [int(input("digite um numero"))for _ in range(5)]

print(f"o menor valor é :{min(lista_valores_numericos)} e sua posiçao na lista é: {lista_valores_numericos.index(min(lista_valores_numericos))}")

print(f"o maior valor é:{max(lista_valores_numericos)} e sua posiçao na lista é {lista_valores_numericos.index(max(lista_valores_numericos))}")






