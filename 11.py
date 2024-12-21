import random

numero_secreto = random.randint(1, 100)

print("Adivina el número; 6 intentos.")

intentos = 6

while intentos > 0:
   
    adivinanza = int(input("Introduce tu número: "))
    
    if adivinanza == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    #profe elif es una abrebiatura de else if que significa en este caso que si es menor el numero que hemos elegido imprime el numero es mayor
    elif adivinanza < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
    
    intentos -= 1
    print("Te quedan {intentos} intentos.")

if intentos == 0:
    print("Has perdido. El número era {numero_secreto}.")
