# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. guarde esses resultados em um dicionario. no final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero do dado.
from random import randint


resultados ={}
    

resultado1 = randint(1,6)
resultado2 = randint(1,6)
resultado3 = randint(1,6)
resultado4 = randint(1,6)

resultados["jogador1"]= resultado1
resultados["jogador2"]= resultado2
resultados["jogador3"]= resultado3
resultados["jogador4"]= resultado4

