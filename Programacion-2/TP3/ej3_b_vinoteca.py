# b. implementar una clase tester que verifique los servicios de la clase Vinoteca

from ej3_a_vinoteca import Vinoteca


class tester:

    # validamos el funcionamiento simulando el uso de la clase Vinoteca

    @staticmethod
    def test_vinoteca():
        # Creamos un objeto de la clase Vinoteca con cantidades iniciales
        vinoteca1 = Vinoteca()

        # Vendemos algunos productos
        vinoteca1.venderJugos(1000)  # Vendemos 1000 unidades de jugos
        vinoteca1.venderVinosBlancos(
            6000
        )  # Intentamos vender 6000 unidades de vinos blancos (solo hay 5000)
        vinoteca1.venderVinosTintosJovenes(
            1000
        )  # Vendemos 1000 unidades de vinos tintos jóvenes
        vinoteca1.venderVinosTintosAnejados(
            4000
        )  # Intentamos vender 4000 unidades de vinos tintos añejados (solo hay 5000)

        # Obtenemos las cantidades restantes de cada producto
        cantJugos = vinoteca1.obtenerCantidadJugos()
        cantBlancos = vinoteca1.obtenerCantidadVinosBlancos()
        cantTintosJovenes = vinoteca1.obtenerCantidadVinosTintosJovenes()
        cantTintosAnejados = vinoteca1.obtenerCantidadVinosTintosAnejados()

        # Imprimimos los resultados
        print(f"Cantidad de jugos restantes: {cantJugos}")
        print(f"Cantidad de vinos blancos restantes: {cantBlancos}")
        print(f"Cantidad de vinos tintos jóvenes restantes: {cantTintosJovenes}")
        print(f"Cantidad de vinos tintos añejados restantes: {cantTintosAnejados}")

        # Reponemos productos
        vinoteca1.reponerJugos()
        vinoteca1.reponerVinosBlancos()
        vinoteca1.reponerVinosTintoJoven()
        vinoteca1.reponerVinosTintoAnejado()

        # Imprimimos los resultados
        print(f"Cantidad de jugos restantes: {cantJugos}")
        print(f"Cantidad de vinos blancos restantes: {cantBlancos}")
        print(f"Cantidad de vinos tintos jóvenes restantes: {cantTintosJovenes}")
        print(f"Cantidad de vinos tintos añejados restantes: {cantTintosAnejados}")


if __name__ == "__main__":
    tester.test_vinoteca()
