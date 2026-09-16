# El mismo almacén del punto anterior almacena los datos del stock de productos en
# el archivo stock.txt separados por punto y coma ( ; ) con el formato “codigo de
# producto; stock mínimo; stock real”. Escriba un programa, que a partir de
# información contenida en los archivos, genere otro archivo de texto, Compras.txt,
# conteniendo todos los productos cuyo stock se encuentra por debajo del mínimo.
# Utilizar el archivo productos.txt del punto anterior, y crear un archivo stock.txt y
# cargarle datos utilizando los códigos de los productos del archivo anterior. Ej:
# 100;50;60
# 102;50;20
# 135;20;15
# 138;20;20
# 140;10;8
# 201;20;30


def leer_stock_desde_archivo(nombre_archivo):
    stock = {}
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                codigo, stock_minimo, stock_real = linea.strip().split(";")
                stock[codigo] = (int(stock_minimo), int(stock_real))
            except ValueError:
                print(f"Error: '{linea.strip()}' no es un formato válido.")
    return stock


def generar_archivo_compras(productos, stock, nombre_archivo_compras):
    with open(nombre_archivo_compras, "w") as archivo_compras:
        for codigo, (stock_minimo, stock_real) in stock.items():
            if stock_real < stock_minimo:
                if codigo in productos:
                    nombre_producto = productos[codigo]
                    archivo_compras.write(
                        f"{codigo};{nombre_producto};{stock_minimo};{stock_real}\n"
                    )


def leer_productos_desde_archivo(nombre_archivo):
    productos = {}
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            try:
                codigo, nombre, precio = linea.strip().split(";")
                productos[codigo] = nombre
            except ValueError:
                print(f"Error: '{linea.strip()}' no es un formato válido.")
    return productos


def main():
    productos = leer_productos_desde_archivo("Programacion-2/TP2/productos.txt")
    stock = leer_stock_desde_archivo("Programacion-2/TP2/stock.txt")
    generar_archivo_compras(productos, stock, "Programacion-2/TP2/Compras.txt")
    print("Archivo Compras.txt generado con éxito.")


if __name__ == "__main__":
    main()
