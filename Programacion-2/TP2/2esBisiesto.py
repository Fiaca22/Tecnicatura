# Escriba una función llamada EsBisiesto que permita ingresar un número de año y
# devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año
# es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre
# 400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por
# pantalla si la fecha es válida o no


def pedir_fecha():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    return dia, mes, anio


def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False


def es_fecha_valida(dia, mes, anio):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    elif mes == 2:
        if es_bisiesto(anio):
            return dia <= 29
        else:
            return dia <= 28
    return False


def main():
    dia, mes, anio = pedir_fecha()
    if es_fecha_valida(dia, mes, anio):
        print("el año es bisiesto" if es_bisiesto(anio) else "el año no es bisiesto")
    else:
        print("La fecha ingresada no es válida.")


main()
