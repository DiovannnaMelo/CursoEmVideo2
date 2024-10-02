#crie um programa onde o usuario possa
#digitar varios valores numericos
#e cadastre-os em uma lista. caso o 
#numero ja exista lá dentro, ele
#nao sera adcionado, no final
#serão exibidos todos os valores unicos
#digitados, em ordem crescente

lista_de_numero = []

while True:
    numero= int(input("digite um numero"))

    if numero not in lista_de_numero:
        lista_de_numero.append(numero)
        print("valor adicionado com sucesso") 
           
    else:
        print("valor duplicado, nao vou adicionar!")

    continuar = input("quer continuar (s/n)?").lower()    
    
    if continuar == "s" :
            continue
    elif continuar == "n":
            break

print (f"todos os valores os valores em ordem crescente são {sorted(lista_de_numero)}")    
        


        
     







    
    

