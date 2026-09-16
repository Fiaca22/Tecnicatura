# Escriba un programa que permita ingresar un número, se debe validar que
# realmente se haya ingresado un número, y crear una lista para almacenar por
# separado los dígitos del número. Luego recorrer la lista y mostrar el índice que
# contiene el dígito mayor.


def pedir_numero():
    numero = input("Ingrese un número: ")
    if numero.isdigit():
        return numero
    else:
        print("Error: Debe ingresar un número válido.")
        return pedir_numero()


def separar_digitos(numero):
    lista_digitos = []
    for digito in numero:
        lista_digitos.append(int(digito))
    return lista_digitos


def buscar_indice_digito_mayor(lista_digitos):
    digito_mayor = max(lista_digitos)
    indice_digito_mayor = lista_digitos.index(digito_mayor)
    return indice_digito_mayor


def main():
    numero = pedir_numero()
    lista_digitos = separar_digitos(numero)
    indice_digito_mayor = buscar_indice_digito_mayor(lista_digitos)
    print(f"El dígito mayor es: {max(lista_digitos)}")
    print(f"Se encuentra en el índice: {indice_digito_mayor + 1}")


main()
