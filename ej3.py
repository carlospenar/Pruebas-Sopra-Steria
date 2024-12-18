# LEER HORASTRABAJADAS y LEER TARIFA
HORASTRABAJADAS = float(input("Ingrese la cantidad de horas trabajadas: "))
TARIFA = float(input("Ingrese la tarifa por hora: "))

# Definir el límite de horas normales
HORASNORMALES = 40
HORASEXTRAS = 0
SUELDO = 0.0

# Calcular el sueldo
if HORASTRABAJADAS > HORASNORMALES:
    # Calcular las horas extras
    HORASEXTRAS = HORASTRABAJADAS - HORASNORMALES
    # Calcular el sueldo con horas extras
    SUELDO = (HORASNORMALES * TARIFA) + (HORASEXTRAS * TARIFA * 1.5)
else:
    # Si no hay horas extras, solo se paga el sueldo normal
    SUELDO = HORASTRABAJADAS * TARIFA

# Mostrar el resultado
print(f"El sueldo total recibido por el trabajador es: {SUELDO:.2f} unidades monetarias.")