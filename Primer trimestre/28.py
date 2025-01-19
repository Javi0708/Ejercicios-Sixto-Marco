def imprimir_menu():
    print("1. Pedir operandos")
    print("2. Sumar")
    print("3. Dividir")
    print("0. Salir")
    print("Opción:")

def sumar(a, b):
    print(f"Resultado de la suma: {a + b}")

def dividir(a, b):
    if b == 0:
        print("Error: División por cero no permitida.")
    else:
        print(f"Resultado de la división: {a / b}")

def main():
    opcion = -1
    a = b = 0

    while opcion != 0:
        imprimir_menu()
        try:
            opcion = int(input())
            if opcion < 0 or opcion > 3:
                print("Opción incorrecta. Intente de nuevo.")
                continue

            if opcion == 1:
                a = int(input("Introduce el primer número: "))
                b = int(input("Introduce el segundo número: "))
            elif opcion == 2:
                sumar(a, b)
            elif opcion == 3:
                dividir(a, b)
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número entero.")

if __name__ == "__main__":
    main()
