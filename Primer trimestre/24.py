frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

if len(letra) != 1:
    print("Debes introducir solo una letra.")
else:
    contador_while = 0
    i = 0
    while i < len(frase):
        if frase[i] == letra:
            contador_while += 1
        i += 1

    contador_for = 0
    for caracter in frase:
        if caracter == letra:
            contador_for += 1

    print(f"Con while, la letra '{letra}' aparece {contador_while} veces.")
    print(f"Con for, la letra '{letra}' aparece {contador_for} veces.")
