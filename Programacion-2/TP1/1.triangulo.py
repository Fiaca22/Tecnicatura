# Realizar un programa que pida los tres lados de un triángulo e indique el tipo de
# triángulo que es según sus lados: Equilátero (tres lados iguales), Isósceles (dos
# lados iguales) o Escaleno (tres lados distintos)
lado1 = float(input("Ingrese el primer lado del triangulo: "))
lado2 = float(input("ingrese el segundo lado del triangulo: "))
lado3 = float(input("Ingrese el tercer lado del triangulo: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es Isosceles")
else:
    print("El triangulo es Escaleno")
