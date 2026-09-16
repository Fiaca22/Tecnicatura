# Escribir un procedimiento “reverso” que permita ingresar como parámetro una
# cadena, y devuelva la cadena invertida (“hola” se convierte en “aloh”). Escribir luego
# un programa que determine si una cadena de caracteres es un palíndromo (un
# palíndromo es un texto que se lee igual en sentido directo y en inverso, ej.: “radar”).
# Sugerencia: para evitar diferencias entre mayúsculas y minúsculas en las cadenas,
# utilice la función del tipo string .upper() ó .lower() en las cadenas, ya que Radar es
# distinto a radaR


def pedir_cadena():
    cadena = input("Ingrese una cadena de caracteres: ").lower()
    return cadena


def reverso(cadena):
    cadena_invertida = ""
    for i in cadena:
        cadena_invertida = i + cadena_invertida
    return cadena_invertida


def es_palindromo(cadena, cadena_invertida):
    if cadena == cadena_invertida:
        return True
    else:
        return False


def main():
    cadena = pedir_cadena()
    cadena_invertida = reverso(cadena)
    print(f"Cadena original: {cadena}")
    print(f"Cadena invertida: {cadena_invertida}")
    if es_palindromo(cadena, cadena_invertida):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")


main()
