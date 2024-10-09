#crie um programa onde o usuario possa digitar
#sete valores numericos e cadastre-os em uma unica
#lista que mantenha separados os valores pares
#e impares. no final, mostre os valores pares 
#e impares em ordem crescente.

numeros=[]
pares=[]
impares=[]

for i in range(7):
    numero = int(input("digite um numero inteiro "))

    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)

numeros.append(pares)
numeros.append(impares)

print(f"os valores pares digitados foram {sorted(pares)}")
print(f"os valores impares digitados foram {sorted(impares)}")



    

