# Dada una cadena de texto ingresada por consola, decir cuántos “espacios” contiene.

cadena = input("Ingrese una cadena de texto: ")
espacios = 0
for caracter in cadena:
    if caracter == " ":
        espacios += 1
print(f"La cadena contiene {espacios} espacios.")

# cadena = input("Ingrese una cadena de texto: ")
# espacios = cadena.count(" ")
# print(f"La cadena contiene {espacios} espacios.")
