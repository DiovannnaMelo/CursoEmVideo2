#Crie um dicionário para armazenar o nome e o preço de cinco produtos.
# Peça ao usuário para inserir o nome de cada produto e o respectivo
# preço. À medida que o usuário fornece os dados, armazene cada 
# produto como uma chave no dicionário e o preço como o valor associado
# a essa chave. Após a inserção de todos os produtos e preços, calcule
# o valor total da compra somando todos os preços armazenados no
# dicionário. Por fim, exiba o valor total da compra.

produto_preco ={}
soma = 0

for i in range(5):
    produto= input("digite o nome do produto")
    preco = float(input("digite o preço do produto"))
    
    produto_preco[produto] = preco

for valor in produto_preco.values():
    soma = soma + valor

print(f" a soma de todos os preços é {soma}")    
      

    
