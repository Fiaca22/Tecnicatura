# Un almacén guarda los códigos, los nombres de los productos y sus precios,
# respectivamente, separados por punto y coma ( ; ) en el archivo productos.txt. Hacer
# un algoritmo y luego los procedimientos necesarios que permitan tomar los datos del
# archivo y buscar el precio de un artículo ingresado por teclado. Para probar el
# algoritmo crear un archivo “productos.txt” y cargarle datos al estilo:
# 100;arroz;10
# 102;fideos;5
# 135;lentejas;8
# 138;porotos;6
# 140;sal gruesa;5
# 201;aceite;20 ( etc… )


def leer_productos_desde_archivo(nombre_archivo):
    productos = {}
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                codigo, nombre, precio = linea.strip().split(";")
                productos[nombre] = float(precio)
            except ValueError:
                print(f"Error: '{linea.strip()}' no es un formato válido.")
    return productos


def buscar_precio_producto(productos, nombre_producto):
    nombre_producto = nombre_producto.lower()
    if nombre_producto in productos:
        return productos[nombre_producto]
    else:
        return None


def main():
    productos = leer_productos_desde_archivo("Programacion-2/TP2/productos.txt")
    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
    precio = buscar_precio_producto(productos, nombre_producto)

    if precio is not None:
        print(f"El precio de '{nombre_producto}' es: {precio}")
    else:
        print(f"El producto '{nombre_producto}' no se encuentra en el almacén.")


if __name__ == "__main__":
    main()
