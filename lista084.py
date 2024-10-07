#faça um programa que leia nome e peso de varias
#pessoas,guardando tudo em uma lista.no final,mostre:
#a)quantas pessoas foram cadastradas.
#b)uma lista com as pessoas mais pesadas.
#c)uma listagem com as pessoas mais leves.

pessoas=[]
nome_peso =[]
pesos=[]
minimos=[]
maximos=[]
nomes_max=[]
nomes_min=[]

#criei a lista pessoas pq eu achei que era p criar uma lista com as informaçoes dentro de nome_peso mais foi uma burrice
#dava p ter criado so a lista nome e a lista
while True:
    nome_peso.append(input("digite nome"))
    nome_peso.append(float(input("digite peso")))
    pessoas.append(nome_peso)
    
    continuar= input("quer continuar s/n ?")

    if continuar.lower()== "s":
        continue
    elif continuar.lower() == "n":
        break

print(f"quantidade de pessoas castradas :{len(pessoas)}")

#adicionando os indices inpares(pq a lista começa em 0 e os indices pares sempre são nomes e os impares pesos)
#  da lista nome_peso na lista pesos para depois conseguir pegar o max

#aqui essa linha a baixo n ta funcionando vc o i ta interando numa lista de string e numeros ai ta dando erro comparando paramentrso de numero com str
for i in nome_peso:
    if i !=0 and i%2==1:
        pesos.append(i)
        

        

for i in pesos:
    if i== max(pesos):  
        maximos.append(i)
        nomes_max.append(nome_peso.index(i))

    elif i== min(pesos):
        minimos.append(i)
        nomes_min.append(nome_peso.index(i))


print(f"o maior peso é {max(pesos)}, peso de{nomes_min} ")

print(f"pessoas mais leves é {max(pesos)}, peso de {nomes_max}")


