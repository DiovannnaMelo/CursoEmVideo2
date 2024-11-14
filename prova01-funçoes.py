# Crie uma função chamada media que receberá três números como argumentos.
#  Esta função deve calcular a média aritmética desses três números. 
# Para fazer isso, some os três números e, em seguida, divida o resultado por três.
#  Por fim, a função deve retornar o valor da média aritmética calculada.

def media (num1,num2,num3):
    media_notas = (num1+ num2 +num3)/3
    return media_notas

n1 = float(input("digite a primeira nota"))
n2 = float(input("digite a segunda nota"))
n3 = float(input("digite a terceira nota"))

resultado= media(n1,n2,n3)
print(f" a média aritméditica das 3 notas são {resultado} ")
