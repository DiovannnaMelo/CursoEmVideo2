
def relogio( horario):
    if horario>= 6 and horario< 12:
        print("bom dia")
    elif horario>= 12 and horario<18:
        print("boa tarde")    
    else:
        print("boa note")    

hora = float(input("digite horario"))

relogio (hora)        