
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)

if numero2 != 0:
    print("División:", numero1 / numero2)
else:
    print("Error: no se puede dividir entre cero.")
