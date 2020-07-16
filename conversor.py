# pesos = input("Ingresa tu cantidad en pesos colombianos: ")
# # casting the pesos a float
# pesos = float(pesos)
# valor_dolar = 3875 
# dolar = pesos / valor_dolar;
# # round recibe el valorr y el numero de decimales
# dolar = round(dolar, 2)
# dolar = str(dolar)
# print(f'Tienes $ {dolar} dolares')


# reto

# funcion de calculo
def convert(actual_coin, new_coin, value):
    if actual_coin == 1 and new_coin == 2:
        # convertir de pesos mexicanos a dolares
        return value * 0.045;
    elif actual_coin == 1 and new_coin == 3:
        # convertir de pesos mexicanos a Pesos colombianos
        return value * 162.42;
    elif actual_coin == 1 and new_coin == 4:
        # convertir de pesos mexicanos a Euros
        return value * 0.039
    elif actual_coin == 2 and new_coin == 1:
        # convertir de  dolares a pesos Mexicanos
        return value * 22.41
    elif actual_coin == 2 and new_coin == 3:
        # convertir de  dolares a pesos Colombianos
        return value * 3640.72
    elif actual_coin == 2 and new_coin == 4:
        # convertir de  dolares a euros
        return value * 0.88
    elif actual_coin == 3 and new_coin == 1:
        # convertir de Pesos Colombianos a pesos Mexicanos
        return value * 0.0062
    elif actual_coin == 3 and new_coin == 2:
        # convertir de pesos colombianos a dolares
        return value * 0.00028
    elif actual_coin == 3  and new_coin == 4:
        # convertir de pesos colombianos a euros
        return value * 0.00024
    elif actual_coin == 4  and new_coin == 1:
        # convertir de Euros a Pesos Mexicanos
        return value * 25.52
    elif actual_coin == 4  and new_coin == 2:
        # convertir de Euros a Dolares
        return value * 1.14
    elif actual_coin == 4  and new_coin == 3:
        # convertir de Euros a pesos Colombianos
        return value * 4145.51
    else:
        return "Trabajando en ello no econtramos tu moneda"


# funcion que determina tipo de moneda
def determineCoin(coin):
    if coin == 1:
        return "Pesos Mexicanos"
    elif coin == 2:
        return "Dolares"
    elif coin == 3:
        return "Pesos Colombianos"
    elif coin == 4:
        return "Euros"
    
# funcion principal
def main():
    still_on = True 

    while(still_on == True):
        # recibiendo inputs
        actual_coin = int(input("Que moneda quieres convertir?\n1-Pesos Mexicanos\n2-Dolares \n3-Pesos Colombianos\n4- Euros\n |"))
        new_coin = int(input("A que moneda quieres convertir?\n1-Pesos Mexicanos\n2-Dolares \n3-Pesos Colombianos\n4- Euros\n |"))

        # calculo
        if(actual_coin != new_coin and actual_coin <= 4 and new_coin <= 4):
            determine_coin = determineCoin(actual_coin)
            determine_next_coin = determineCoin(new_coin)
            amount = int(input(f"Cuantos {determine_coin} tienes?   "))
            result = convert(actual_coin, new_coin, amount)
            print(f"Tienes {round(result, 2)} {determine_next_coin}")
        elif(actual_coin > 4 or new_coin > 4):
            print("Opcion invalida")
        else:
            print("Elegiste la misma moneda en ambos casos no me quieras trolear")

        # para continuar o salir
        res = input("Deseas continuar.. y/n   ")
        if(res == "y"):
            still_on = True
        elif (res == "n"):
            still_on = False
            print("Espero haber ayudado uwu")
        else:
            res = input("Deseas continuar.. y/n   ")
            if(res != "y" or "n"):
                print("adios no me sabes usar")
                still_on = False


main()











