# Escriba un programa que permita cargar las notas de exámenes, primero debe
# permitir ingresar por teclado la cantidad de notas que desea cargar, y luego
# cargarlas en una lista, y posteriormente debe buscar la nota más alta, mostrarla, e
# indicar en qué índice del arreglo se encuentra


def cargar_notas():
    cantidad = int(input("Ingrese la cantidad de notas que desea cargar: "))
    notas = []
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        notas.append(nota)
    return notas


def buscar_nota_mas_alta(notas):
    nota_mas_alta = 0
    for i in notas:
        if i > nota_mas_alta:
            nota_mas_alta = i
    return nota_mas_alta


def main():
    notas = cargar_notas()
    nota_mas_alta = buscar_nota_mas_alta(notas)
    indice_nota_mas_alta = notas.index(nota_mas_alta)
    print(f"La nota más alta es: {nota_mas_alta}")
    print(f"Se encuentra en el índice: {indice_nota_mas_alta + 1}")


main()
