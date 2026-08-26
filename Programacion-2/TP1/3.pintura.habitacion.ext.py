# Extienda el programa anterior para permitir múltiple cantidad de “manos” de pintura.

ancho = float(input("Ingrese el ancho de la habitacion en metros: "))
alto = float(input("Ingrese el alto de la habitacion en metros: "))
largo = float(input("Ingrese el largo de la habitacion en metros: "))

superficie_paredes = 2 * (ancho * alto + largo * alto)

superficie_puerta = 0.8 * 2

superficie_total = superficie_paredes - superficie_puerta

pintura_nesesaria = superficie_total / 10

manos = int(input("Ingrese la cantidad de manos de pintura que desea aplicar: "))

pintura_nesesaria *= manos

print(f"Se necesitan {pintura_nesesaria} litros de pintura para pintar la habitacion")
