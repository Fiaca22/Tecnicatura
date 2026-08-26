# Implemente un programa que a partir del ancho, alto y largo de una habitación
# rectangular calcule cuántos litros de pintura se necesitan para pintarla. Suponiendo
# que 1 litro de pintura sirve para 10m cuadrados y que la habitación tiene sólo una
# puerta de 0,80 de ancho por 2 mts de alto

ancho = float(input("Ingrese el ancho de la habitacion en metros: "))
alto = float(input("Ingrese el alto de la habitacion en metros: "))
largo = float(input("Ingrese el largo de la habitacion en metros: "))

superficie_paredes = 2 * (ancho * alto + largo * alto)

superficie_puerta = 0.8 * 2

superficie_total = superficie_paredes - superficie_puerta

pintura_nesesaria = superficie_total / 10

print(f"Se necesitan {pintura_nesesaria} litros de pintura para pintar la habitacion")
