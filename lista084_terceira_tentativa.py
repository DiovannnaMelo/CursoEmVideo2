#faça um programa que leia nome e peso de varias
#pessoas,guardando tudo em uma lista.no final,mostre:
#a)quantas pessoas foram cadastradas.
#b)uma lista com as pessoas mais pesadas.
#c)uma listagem com as pessoas mais leves

nome_peso =[]
pessoas_max=[]
pessoas_min=[]
pesos=[]
while True:
   nome= input("digite o nome: ")
   peso = float(input("digite o seu seu peso: "))
   nome_peso.append([nome,peso])

   continuar= input("quer continuar s/n ?")

   if continuar.lower()=="s":
      continue
   elif continuar.lower()=="n":
      break
   
print(f"quantidade de pessoas cadastradas {len(nome_peso)}") 

for peso in nome_peso:
   pesos.append(peso[1])

for i in nome_peso:
    if i[1]== max(pesos):
       pessoas_max.append(i[0])
    
    elif i[1]== min(pesos):
       pessoas_min.append(i[0])

print(f"o peso max é {max(pesos)}, é o peso de {pessoas_max}")

print(f"o peso max é {min(pesos)}, é o peso de {pessoas_min}")



