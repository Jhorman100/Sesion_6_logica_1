num_1 = float(input("Primer numero a consultar "))
num_2 = float(input("Segundo numero a consultar "))
operador = input("Que operacion vas a hacer? (+,-,/,*): ")

if operador == "+":
    print("Resultado", num_1 + num_2)
elif operador == "-":
    print("Resultado", num_1 - num_2)
elif operador == "*":
    print("Resultado", num_1 * num_2)
elif operador == "/":
    if num_2 != 0:
        print("Resultado", num_1 / num_2)
    else:
        print("Error dividiendo por cero")
else:
    print("operacion no valida")
