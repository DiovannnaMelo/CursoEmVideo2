#crie um programa que vai ler varios numeros 
#e colocar em uma lista. depois disso,mostre:
#a)quantos numeros foram digitados
#b)a lista de valores,ordenada de forma
#decrescente.
#c) se valor 5 foi digitado e esta ou nao na lista

lista=[]

while True:
    numero= int(input("digite um numero inteiro"))
    lista.append(numero)
    continuar = input("digite se que continuar (s/n)") 

    if continuar.lower() =="s":
        continue
    elif continuar.lower()== "n":
        break

print(f"a quantidade de numeros digitados foram {len(lista)} ")

print(f"lista de valores em ordem decrescente é {sorted(lista,reverse=True)}")

if 5 in lista:
    print("o valor 5 esta na lista")

else:
    print("o valor 5 não esta na lista")



    
