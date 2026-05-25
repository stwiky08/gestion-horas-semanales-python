# Función para calcular el total de horas y clasificar la jornada
def calcular_horas(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion


# Matriz con 4 recursos y horas trabajadas de lunes a viernes
recursos = [
    ["Juan", 8, 9, 8, 9, 8],
    ["María", 7, 8, 8, 8, 7],
    ["Carlos", 9, 9, 9, 8, 9],
    ["Ana", 8, 8, 8, 8, 8]
]

# Procesar e imprimir resultados
print("REPORTE DE HORAS SEMANALES\n")

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_horas(horas)

    print(f"Recurso: {nombre}")
    print(f"Total de horas semanales: {total}")
    print(f"Clasificación: {clasificacion}")
    print("-" * 30)
