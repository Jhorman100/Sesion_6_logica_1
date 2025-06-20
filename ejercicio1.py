# Implementar una calculadora que pida dos numeros y una operacion,
# vamos a usar la figura de switch...case y luego con if...elif...else.

#calculadora basica:


num_1 = float(input("Primer numero a consultar "))
num_2 = float(input("Segundo numero a consultar "))
operador = input("Que operacion vas a hacer? (+,-,/,*): ")

# Como asi que switch y case
# switch y case es una forma diferente de escribir condicionales, 
# donde se evalua un parametro, boolenao, y se va a direccionar 
# inmediantemente segun los casos definidos


match operador:
    case "+":
        print("Resultado", num_1 + num_2)
    case "-":
        print("Resultado", num_1 - num_2)
    case "*":
        print("Resultado", num_1 * num_2)
    case "/":
        if num_2 != 0:
            print("Resultado", num_1 / num_2)
        else:
            print("Resultado no valido")
    case _:
        print("Resultado no valido")
