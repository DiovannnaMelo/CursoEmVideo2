#crie um programa que vai ler varios numeros e 
#colocar em uma lista. depois disso,crie duas listas
#extras que vao conter apenas os valores pares e os
#valores impares digitados,respectivamente.
#ao final,mostre o conteudo das tres listas geradas.

lista=[]
lista_pares=[]
lista_inpares=[]
while True:
    numero= int(input("digite um numero inteiro: "))
    lista.append(numero)
    continuar= input("digite se que continuar (s/n)?")

    if numero%2==0:
        lista_pares.append(numero)

    else:
        lista_inpares.append(numero)
    
    if continuar.lower() =="s":
        continue
    elif continuar.lower()=="n":
        break
    

       
print(f"a lista de numeros é: {lista}")
print(f"a lista de numero pares é: {lista_pares}")
print(f"a lista de numeros inpares é: {lista_inpares}")


