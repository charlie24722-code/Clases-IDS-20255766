monto = float(input("Digite el monto: "))
tipo = input("Ingrese el tipo (Local/Export): ")
impuesto = 0

if tipo.lower() == "local":
    if monto > 500:
        impuesto = 0.10
    else: 
        if monto > 200:
            impuesto = 0.08
        else:
            if monto > 50:
                impuesto = 0.06
            else:
                impuesto = 0
elif tipo.lower() == "export":
    if monto > 500:
        impuesto = 0.14
    else: 
        if monto > 200:
            impuesto = 0.12
        else:
            if monto > 50:
                impuesto = 0.1
            else:
                impuesto = 0
else:
    print("Ese tipo no es valido (Sea serio)")
print(f"El impuesto a pagar de {tipo} por venta de {monto:,.2f}")
print(f"es de {monto*impuesto:,.2f}")                















 