#faça um programa que leia nome e média de um aluno,
#guardando tb a situação em um dicionario. no final,
#mostre o conteudo da estrutura na tela.

dicionario={}

dicionario["nome"]= input("digite o seu nome")
dicionario["média"]= float(input("digite o sua média"))

if dicionario["média"]>=7:
    dicionario["situação"]= "aprovado"
else:
    dicionario["situação"]= "reprovado" 

print(dicionario)