color_favorito = input("Introduce tu color favorito: ")

colores_asociados = {
    "rojo": "PASIÓN",
    "amarillo": "FELICIDAD",
    "verde": "ESPERANZA",
    "azul": "CALMA",
    "morado": "CREATIVIDAD"
}

if color_favorito in colores_asociados:
    print(colores_asociados[color_favorito])
else:
    print("Error: color no reconocido")