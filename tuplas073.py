vinte_primeiros_colocados= ("corinthians", "palmeiras", "santos"
,"gremio","cruzeiro","flamengo","vasco",
"chapecoense","atletico","botafogo","nautico",
"sport","santa","baia","time15","time16","time17"
,"time18","time19","time20"
                            )

# o print("-="*15) serve para separar no terminal os prints p ficar mais organizado
print(f" os 5 primeiros colocados são {vinte_primeiros_colocados[0:5]}")
print("-="*15)

print(f" os ultimos 4 colocados são {vinte_primeiros_colocados[-4:]}")
print("-="*15)

print(f" a lista de times em ordem alfabetica {(sorted(vinte_primeiros_colocados))}")
print("-="*15)

#aqui eu tenho que colocar("chapecoense")+1 pq ele começa os indices por 0 entao ele diz que chapecoense
#esta no 7 lugar quando na vd esta no 8, entao so colocamos +1 p resolver isso
print(f" o chapecoense esta na posição {vinte_primeiros_colocados.index("chapecoense")+1}")
print("-="*15)




