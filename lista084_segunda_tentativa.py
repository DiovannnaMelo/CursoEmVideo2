#faça um programa que leia nome e peso de varias
#pessoas,guardando tudo em uma lista.no final,mostre:
#a)quantas pessoas foram cadastradas.
#b)uma lista com as pessoas mais pesadas.
#c)uma listagem com as pessoas mais leves

nome_peso =[]
pessoas_max=[]
pessoas_min=[]
while True:
   nome= input("digite o nome: ")
   peso =float(input("digite o seu seu peso: "))
   nome_peso.append([nome,peso])

   continuar= input("quer continuar s/n ?")

   if continuar.lower()=="s":
      continue
   elif continuar.lower()=="n":
      break
   
print(f"quantidade de pessoas cadastradas {len(nome_peso)}") 

for p in peso:
   if max(peso)==p:
      i= peso.index(p)
      pessoas_max.append(nome.index(p))

   elif min(peso)==p:
      i= peso.index(p)
      pessoas_min.append(nome.index(p))

print(f"peso maximo é {max(peso)}, peso de {pessoas_max}")
print(f"peso minimo é {min(peso)}, peso de {pessoas_min}")

# File "c:\Users\Aluno Infinity\Nova pasta (3)\CursoEmVideo2\lista084_melhorado.py", line 24, in <module>for p in peso:
#^^^^TypeError: 'float' object is not iterable deu esse erro aaaaaaaa


            
      
      
      

   











