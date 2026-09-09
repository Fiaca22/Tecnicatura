# Escriba un programa que permita leer de un archivo distancias.txt (cada renglón
# tiene una distancia válida) las distancias recorridas por el vehículo de una empresa,
# luego calcular cual es la distancia promedio, y mostrar por pantalla el promedio y
# todas las distancias mayores al promedio.
# Ej del contenido del archivo:
# 150
# 120
# 50
# 34
# 250
# Salida: “La distancia promedio de los viajes es … y los viajes con distancia mayor
# son: … , … , …. , …. “


def leer_distancias_desde_archivo(nombre_archivo):
    distancias = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                distancia = float(linea.strip())
                distancias.append(distancia)
            except ValueError:
                print(f"Error: '{linea.strip()}' no es una distancia válida.")
    return distancias


def calcular_promedio(distancias):
    if len(distancias) == 0:
        return 0
    promedio = sum(distancias) / len(distancias)
    return promedio


def filtrar_distancias_mayores_al_promedio(distancias, promedio):
    mayores = []
    for d in distancias:
        if d > promedio:
            mayores.append(d)
    return mayores


def main():
    distancias = leer_distancias_desde_archivo("Programacion-2/TP2/distancias.txt")
    promedio = calcular_promedio(distancias)
    mayores_al_promedio = filtrar_distancias_mayores_al_promedio(distancias, promedio)

    print(f"La distancia promedio de los viajes es: {promedio}")
    if mayores_al_promedio:
        print(
            "Los viajes con distancia mayor al promedio son:",
            ", ".join(map(str, mayores_al_promedio)),
        )
    else:
        print("No hay viajes con distancia mayor al promedio.")


if __name__ == "__main__":
    main()
