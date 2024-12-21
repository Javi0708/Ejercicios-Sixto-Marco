
meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
         7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if 1 <= mes <= 12 and 1 <= dia <= 31:
    if mes in [4, 6, 9, 11] and dia > 30:
        print("Fecha no válida.")
    elif mes == 2 and dia > 29:
        print("Fecha no válida.")