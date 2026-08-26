# Escriba un programa que dado un texto ingresado por el usuario cuente la cantidad
# total de vocales que aparecen y lo muestre por pantalla.

texto = input("Ingrese un texto: ")
vocales = "aeiouAEIOU"
contador = 0

for caracter in texto:
    if caracter in vocales:
        contador += 1

print(f"La cantidad de vocales en el texto es: {contador}")
