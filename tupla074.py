#crie um programa que gere numeros aleatorios
#e coloque numa tupla, depois mostre a listagem
#dos numeros gerados e tb indique o menor e o maior
import random

tupla_numeros_inteiros_aletorios= tuple(random.randint(1,100) for _ in range(5))

print(f"esses são os numeros da tupla {tupla_numeros_inteiros_aletorios}")

print(f" menor valor da tupla é {min(tupla_numeros_inteiros_aletorios)}")

print(f"o maior valor da tupla é {max(tupla_numeros_inteiros_aletorios)} ")

