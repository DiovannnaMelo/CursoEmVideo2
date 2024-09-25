# leia quatro valores pelo teclado e guarde-os em uma tupla
#no final mostre: a) quantas vezes apareceu o valor 9
#b) em que posiçaõ foi digitado o primeiro valor 3
#c) quais foram os numeros pares

tupla_numeros_digitados= tuple(int(input("digite um numero")) for _ in range(4))

print(f"o valor 9 apreceu {tupla_numeros_digitados.count(9)} vezes")

if 3 in tupla_numeros_digitados:
    print(f"o valor 3 foi digitado na posição{tupla_numeros_digitados.index(3)}")
else:
    print("o numero 3 nao esta na sua tupla")    

#em tuple eu crio uma tupla
#no primeiro "num for" eu add num na tupla em uma interação em que cada num da tupla original for par 

print(f"os numeros pares da sua tupla são: {tuple(num for num in tupla_numeros_digitados if num % 2 ==0)}")
