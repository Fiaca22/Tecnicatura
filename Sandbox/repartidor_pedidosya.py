# un repartidor de pedidosya desea registrar el dinero recaudado y la cantidad de viajes que realiza en un turno.
# por cada viaje:
# gana $500 por km recorrido
# a partir del 3km, gana un extra de $100 por cada km adicional
# implemente la clase repartidor y verifique su funcionamiento implementando una clase tester


class repartidor:

    __valorKm = 500
    __valorKmExtra = 100

    # cobros list almacena el monto ganado en cada viaje en una lista

    def __init__(
        self, nombre: str, edad: int, cobros: list = None, pedidosEntregados: int = 0
    ):

        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(edad, int):
            raise TypeError("La edad debe ser un número entero.")
        if cobros is not None and not isinstance(cobros, list):
            raise TypeError("Los cobros deben ser una lista.")
        if not isinstance(pedidosEntregados, int):
            raise TypeError(
                "La cantidad de pedidos entregados debe ser un número entero."
            )

        self.__nombre = nombre
        self.__edad = edad
        if cobros is not None:
            self.__cobros = cobros
        else:
            self.__cobros = []
        self.__pedidosEntregados = pedidosEntregados

    # calcularViaje (km float, propina float=0) calcula el valor del viaje, la propina es opcional +500 por km y
    # a partir del 3km, gana un extra de $100 por cada km adicional

    def calcular_viaje(self, km: float, propina: float = 0):
        if not isinstance(km, (int, float)):
            raise TypeError("Los kilómetros deben ser un número.")
        if not isinstance(propina, (int, float)):
            raise TypeError("La propina debe ser un número.")

        if km <= 3:
            valor_viaje = km * self.__valorKm
        else:
            valor_viaje = (3 * self.__valorKm) + (
                (km - 3) * (self.__valorKm + self.__valorKmExtra)
            )
            valor_viaje += propina
        return valor_viaje

    # hacerViaje (km float, propina float=0) agrega + dinero del viaje a la lista cobros y +1 a viajes y pedidos entregados

    def hacer_viaje(self, km: float, propina: float = 0):
        if not isinstance(km, (int, float)):
            raise TypeError("Los kilómetros deben ser un número.")
        if not isinstance(propina, (int, float)):
            raise TypeError("La propina debe ser un número.")

        valor_viaje = self.calcular_viaje(km, propina)
        self.__cobros.append(valor_viaje)
        self.__pedidosEntregados += 1

    def obtener_nombre(self):
        return self.__nombre

    def obtener_edad(self):
        return self.__edad

    def obtener_pedidos_entregados(self):
        return self.__pedidosEntregados

    # obtener_recaudacion() float retorna la suma de toda la recaudacion

    def obtener_recaudacion(self):
        return sum(self.__cobros)
