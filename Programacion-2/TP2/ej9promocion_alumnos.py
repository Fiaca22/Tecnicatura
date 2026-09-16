# Un profesor almacenó los datos de los alumnos de su materia en un archivo
# alumnos.txt. En cada línea guardó el número de legajo del alumno y sus tres notas
# finales (oral, escrito y trabajos prácticos). El archivo está ordenado por número de
# legajo.
# En otro archivo, ordenado alfabéticamente por apellido, guarda por línea, número de
# legajo, apellido y nombre de cada uno.
# En ambos archivos los datos están separados por punto y coma ( ; ) .
# Desea escribir un programa para generar un archivo Promoción.txt con los apellidos
# y nombres de los alumnos que promocionan la materia, esto es, alumnos que el
# promedio de las tres notas supere los 7 puntos.
# El archivo debe quedar ordenado alfabéticamente


def leer_alumnos_desde_archivo(nombre_archivo):
    alumnos = {}
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                legajo, nota1, nota2, nota3 = linea.strip().split(";")
                promedio = (float(nota1) + float(nota2) + float(nota3)) / 3
                alumnos[legajo] = promedio
            except ValueError:
                print(f"Error: '{linea.strip()}' no es un formato válido.")
    return alumnos


def leer_nombres_desde_archivo(nombre_archivo):
    nombres = {}
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                legajo, apellido, nombre = linea.strip().split(";")
                nombres[legajo] = f"{apellido}, {nombre}"
            except ValueError:
                print(f"Error: '{linea.strip()}' no es un formato válido.")
    return nombres


def generar_archivo_promocion(alumnos, nombres, nombre_archivo_promocion):
    promocionados = []
    for legajo, promedio in alumnos.items():
        if promedio >= 7:
            if legajo in nombres:
                promocionados.append(nombres[legajo])

    promocionados.sort()  # Ordenar alfabéticamente
    with open(nombre_archivo_promocion, "w") as archivo_promocion:
        for nombre_completo in promocionados:
            archivo_promocion.write(f"{nombre_completo}\n")


def main():
    alumnos = leer_alumnos_desde_archivo("Programacion-2/TP2/alumnos.txt")
    nombres = leer_nombres_desde_archivo("Programacion-2/TP2/nombres.txt")
    generar_archivo_promocion(alumnos, nombres, "Programacion-2/TP2/promocion.txt")

    # IMPRESIONES DE DIAGNÓSTICO
    print(f"Alumnos/Notas leídos: {len(alumnos)}")
    print(f"Nombres leídos: {len(nombres)}")
    print("Archivo Promoción.txt generado con éxito.")


if __name__ == "__main__":
    main()
