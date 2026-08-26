# Escriba un programa que permita al usuario ingresar las medidas de 2 lados de un
# rectángulo, y que luego mediante la impresión repetida de un caracter (ej: *) lo dibuje
# en la pantalla. Para este ejercicio tomaremos un máximo de 40 para el lado más
# largo, con el fin de evitar problemas de visualización en la consola. Verificar en los
# datos de entrada que se cumpla este requisito.

largo = int(input("Ingrese el largo del rectángulo (máximo 40): "))
ancho = int(input("Ingrese el ancho del rectángulo (máximo 40): "))

if 1 <= largo <= 40 and 1 <= ancho <= 40:
    for i in range(ancho):
        print("*" * largo)
else:
    print("Error: Los valores ingresados no cumplen con el requisito de máximo 40.")
