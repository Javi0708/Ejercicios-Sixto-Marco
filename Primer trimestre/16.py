def mostrar_menu():
    print("1. Pedir operandos")
    print("2. Sumar")
    print("3. Dividir")
    print("0. Salir")
    return input("Opción: ")

def pedir_operandos():
    global operando1, operando2
    operando1 = int(input("Introduce el primer operando: "))
    operando2 = int(input("Introduce el segundo operando: "))

def sumar():
    print(f"Resultado de la suma: {operando1 + operando2}")

def dividir():
    if operando2 == 0:
        print("Error: División por cero no permitida.")
    else:
        print(f"Resultado de la división: {operando1 / operando2}")

operando1 = 0
operando2 = 0

while True:
    opcion = mostrar_menu()
    if opcion.isdigit() and 0 <= int(opcion) <= 3:
        opcion = int(opcion)
        if opcion == 1:
            pedir_operandos()
        elif opcion == 2:
            sumar()
        elif opcion == 3:
            dividir()
        elif opcion == 0:
            print("Saliendo del programa...")
            break
    else:
        print("Opción incorrecta. Por favor, elige una opción entre 0 y 3.")