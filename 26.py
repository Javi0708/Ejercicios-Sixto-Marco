def main():
    print("¡Hola! ¿Cómo te llamas?")
    nombre = input("Por favor, introduce tu nombre: ")
    print(f"¡Encantado de conocerte, {nombre}!")

    while True:
        print("\n¿Qué quieres saber sobre la Informática?")
        print("Puedes introducir las palabras CITA, DATO o ANÉCDOTA.")
        print("Escribe 'SALIR' para terminar la conversación.")
        eleccion = input("Tu elección: ").strip().upper()

        if eleccion == "CITA":
            print("“Si piensas que los usuarios de tus programas son idiotas, sólo los idiotas usarán tus programas” – Linus Torvalds")
        elif eleccion == "DATO":
            print("El código binario es el lenguaje de las máquinas.")
        elif eleccion == "ANÉCDOTA":
            print("Ada Lovelace fue una matemática británica considerada la primera persona que escribió un algoritmo destinado a ser procesado por una máquina.")
        elif eleccion == "SALIR":
            print("¡Hasta luego! Ha sido un placer hablar contigo.")
            break
        else:
            print("Lo siento, no entiendo tu elección. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()