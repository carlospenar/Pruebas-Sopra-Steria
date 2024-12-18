# LEER NUMERO (Entrada de datos al inicio)
NUMERO = int(input("Ingrese un número entero: "))

# Verificar si el número es par o impar
if NUMERO % 2 == 0:
    # Si el número es par, imprimir los números pares de manera descendente desde NUMERO hasta 0
    for i in range(NUMERO, -1, -2):
        print(i)
else:
    # Si el número es impar, imprimir los números impares de manera descendente desde NUMERO hasta 1
    for i in range(NUMERO, 0, -2):
        print(i)
