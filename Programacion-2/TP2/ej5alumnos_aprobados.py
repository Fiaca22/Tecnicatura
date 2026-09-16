# Escriba un programa que permita cargar una lista de alumnos junto con su nota del
# parcial. Seleccione la estructura de datos que mejor se adapte al problema. Luego
# de ingresados los datos debe generar una lista donde figure si aprobaron o no (se
# aprueba con 40 o más). El listado a mostrar por pantalla debe ser como el siguiente
# (el resultado no se almacena, se calcula):
# ALUMNOS PARCIAL RESULTADO
# Smith, Juan 70 Aprobado
# Suárez, María 35 Desaprobado


def cargar_alumnos():
    cantidad = int(input("Ingrese la cantidad de alumnos que desea cargar: "))
    alumnos = []
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        nota = int(input(f"Ingrese la nota del parcial de {nombre}: "))
        if nota < 0 or nota > 100:
            print("Error: La nota debe estar entre 0 y 100.")
            return cargar_alumnos()
        alumnos.append((nombre, nota))
    return alumnos


def mostrar_resultados(alumnos):
    print("ALUMNOS\t\tPARCIAL\tRESULTADO")
    for alumno in alumnos:
        nombre, nota = alumno
        resultado = "Aprobado" if nota >= 40 else "Desaprobado"
        print(f"{nombre}\t        {nota}\t{resultado}")


def main():
    alumnos = cargar_alumnos()
    mostrar_resultados(alumnos)


main()
