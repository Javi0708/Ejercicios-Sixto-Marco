def chatbot():
    option1 = True
    option2 = True
    option3 = True

    while True:
        print("1. Saludo")
        print("2. Pregunta")
        print("3. Despedida")
        print("4. Salir")
        choice = input("Elige una opción: ")

        if choice == "1":
            if option1:
                print("¡Hola! ¿Cómo estás?")
            else:
                print("¡Hola de nuevo! ¿Cómo te va?")
            option1 = not option1

        elif choice == "2":
            if option2:
                print("¿En qué puedo ayudarte?")
            else:
                print("¿Tienes alguna duda?")
            option2 = not option2

        elif choice == "3":
            if option3:
                print("¡Adiós! Que tengas un buen día.")
            else:
                print("¡Hasta luego! Cuídate.")
            option3 = not option3

        elif choice == "4":
            print("Saliendo del chatbot. ¡Hasta la próxima!")
            break

        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    chatbot()