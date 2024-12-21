dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))
while True:
    if divisor != 0:
        break #la instrucción break le proporciona la oportunidad de cerrar un bucle cuando se activa una condición externa, es como si anulara
    print("Intentalo de nuevo.")

resultado = dividendo / divisor
print("El resultado es: {resultado}")