saldo = float(input("Saldo: "))
cheque = float(input("Cheque: "))
print("Fondos insuficientes" if cheque > saldo else "Cantidad descontada")