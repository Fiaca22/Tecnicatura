# Se desea realizar una aplicación que solicite al usuario tres números enteros
# positivos (A, B, y X), y que muestre por pantalla todos los múltiplos de X que estén
# entre A y B inclusive

print(
    "Ingrese tres números enteros positivos (A, B, y X) para mostrar todos los múltiplos de X que estén entre A y B inclusive."
)
A = int(input("Ingrese el primer número (A): "))
B = int(input("Ingrese el segundo número (B): "))
X = int(input("Ingrese el tercer número (X): "))

for i in range(A, B + 1):
    if i % X == 0:
        print(i, end=" ")
