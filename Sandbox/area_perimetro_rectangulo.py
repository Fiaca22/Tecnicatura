# pedir al usuario el valor de la base y la altura del rectángulo
base = float(input("Ingrese el valor de la base del rectángulo: "))
altura = float(input("Ingrese el valor de la altura del rectángulo: "))
# calcular el área del rectángulo
area = base * altura
# calcular el perímetro del rectángulo
perimetro = 2 * (base + altura)
# mostrar los resultados al usuario
print("El área del rectángulo es:", area)
print("El perímetro del rectángulo es:", perimetro)