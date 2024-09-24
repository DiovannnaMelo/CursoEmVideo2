
contagem= ("zero","um","dois","tres","quatro","cinco","seis","oito","nove",
           "dez","onze","treze","quatoze","quinze","dezeseis",
           "dezesete","dezoito","dezenove","vinte")

while True:
    numero= int(input("digite um numero de 0 a 20"))
    if numero >=0 and numero <=20:
            print(f" vc digitou o numero {contagem[numero]} ")
            break

    else:
          print("tente novamente,digite um numero entre 0 e 20")

        

