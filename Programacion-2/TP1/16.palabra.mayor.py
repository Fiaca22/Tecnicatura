# Escriba un programa que para un texto ingresado nos muestre cual es la palabra
# más larga dentro de ese texto y cuántas letras tiene

texto = input("Ingrese un texto: ")
palabras = texto.split()
palabra_mas_larga = ""
for palabra in palabras:
    if len(palabra) > len(palabra_mas_larga):
        palabra_mas_larga = palabra

print(
    f"La palabra más larga es: '{palabra_mas_larga}' con {len(palabra_mas_larga)} letras."
)
