# Escriba un programa que, dada una oración ingresada muestre por pantalla:
# a. El número total de caracteres en la oración
# b. La cantidad total de letras (consonantes y vocales, sin signos de puntuación)
# c. La cantidad de palabras separadas por uno o más espacios
# En este ejercicio, para simplificar, asumiremos que los posibles caracteres de
# entrada son letras, espacios, dígitos, signos de puntuación, signos de
# interrogación y de exclamación.
# Investigar si hay funciones de strings que nos faciliten la resolución [len(),
# .isalpha(), .split() , etc.]

oracion = input("Ingrese una oración: ")
# a. Número total de caracteres
total_caracteres = len(oracion)
# b. Cantidad total de letras (consonantes y vocales)
cantidad_letras = sum(1 for caracter in oracion if caracter.isalpha())
# c. Cantidad de palabras separadas por uno o más espacios
palabras = oracion.split()
cantidad_palabras = len(palabras)

print(f"Número total de caracteres: {total_caracteres}")
print(f"Cantidad total de letras: {cantidad_letras}")
print(f"Cantidad de palabras: {cantidad_palabras}")
