from repartidor_pedidosya import repartidor


class tester:

    # validamos el funcionamiento simulando el uso de la clase repartidor

    @staticmethod
    def test_repartidor():
        # Creamos un objeto de la clase repartidor
        repartidor1 = repartidor("Juan", 25)

        # Simulamos algunos viajes
        repartidor1.hacer_viaje(2)  # Viaje de 2 km sin propina
        repartidor1.hacer_viaje(4, 50)  # Viaje de 4 km con propina de $50
        repartidor1.hacer_viaje(5)  # Viaje de 5 km sin propina

        # Obtenemos la recaudación total y la cantidad de pedidos entregados
        recaudacion_total = repartidor1.obtener_recaudacion()
        pedidos_entregados = repartidor1.obtener_pedidos_entregados()

        # obtenemos ifnormación del repartidor
        nombre = repartidor1.obtener_nombre()
        edad = repartidor1.obtener_edad()

        # Imprimimos los resultados
        print(f"Nombre del repartidor: {nombre}")
        print(f"Edad del repartidor: {edad}")
        print(f"pedidos entregados: {pedidos_entregados}")
        print(f"Recaudación total: ${recaudacion_total}")


if __name__ == "__main__":
    tester.test_repartidor()
