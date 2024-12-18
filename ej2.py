import random

# Definir una estructura para representar a las personas
class Persona:
    def __init__(self, sexo, edad):
        self.sexo = sexo
        self.edad = edad

# LEER PERSONAS: Cargar los datos de 50 personas
PERSONAS = []
for i in range(50):
    sexos = ["M", "F"] 
    sexo = random.choice(sexos)
    edad = random.randint(1, 100)
    #Se resuleve el ejercicio introduciendo una clasificación de personas obtenida de forma aleatoria, para así comprobar el funcionamiento del algoritmo de forma más rápida y eficiente
    PERSONAS.append(Persona(sexo, edad))

# Inicializar contadores
mayores_edad = 0
menores_edad = 0
masculinos_mayores = 0
femeninas_menores = 0
total_personas = 50
mujeres = 0

# Recorrer la lista de PERSONAS y actualizar los contadores
for persona in PERSONAS:
    if persona.edad >= 18:
        mayores_edad += 1
        if persona.sexo == 'M':
            masculinos_mayores += 1
    else:
        menores_edad += 1
        if persona.sexo == 'F':
            femeninas_menores += 1
    
    if persona.sexo == 'F':
        mujeres += 1

# Calcular porcentajes
porcentaje_mayores_edad = (mayores_edad / total_personas) * 100
porcentaje_mujeres = (mujeres / total_personas) * 100

# Mostrar los resultados
print("\nResultados:")
print(f"A) Cantidad de personas mayores de edad: {mayores_edad}")
print(f"B) Cantidad de personas menores de edad: {menores_edad}")
print(f"C) Cantidad de personas masculinas mayores de edad: {masculinos_mayores}")
print(f"D) Cantidad de personas femeninas menores de edad: {femeninas_menores}")
print(f"E) Porcentaje de personas mayores de edad respecto al total: {porcentaje_mayores_edad:.2f}%")
print(f"F) Porcentaje de mujeres respecto al total: {porcentaje_mujeres:.2f}%")