# Una vinoteca tiene su depósito dividido en cuatro grandes secciones: Jugos sin
# alcohol, Vinos blancos, Vinos tintos jóvenes y Vinos tintos añejados. Cada sección
# del depósito puede almacenar un máximo de 5000 unidades de su respectivo
# producto. Al crearse la vinoteca, cada sección comienza con su capacidad máxima.
# La vinoteca puede vender productos de cualquiera de las cuatro secciones, lo que
# reduce la cantidad disponible en esa sección. Si la cantidad solicitada es mayor a la
# disponible en una sección, se vende lo que se pueda y se informa que no se pudo
# completar la venta. Además, es posible reponer la cantidad de un producto en una
# sección hasta alcanzar su capacidad máxima. Cada vinoteca puede modelarse con
# el siguiente diagrama:
# a. implementar en python la clase vinoteca
# b. implementar una clase tester que verifique los servicios de la clase Vinoteca
# con valores significativos.

# Vinoteca

# <<atributos de clase>>
# - capacidadMaxima: int

# <<atributos de instancia>>
# - cantJugos: int
# - cantBlancos: int
# - cantTintosJovenes: int
# - cantTintosAnejados: int

# <<constructores>>
# + vinoteca()

# <<comandos>>
# + reponerJugos()
# + reponerVinosBlancos()
# + reponerVinosTintoJoven()
# + reponerVinosTintoAnejado()
# + venderJugos(unidades: int)
# + venderVinosBlancos(unidades: int)
# + venderVinosTintosJovenes(unidades: int)
# + venderVinosTintosAnejados(unidades: int)

# <<consultas>>
# + obtenerCantidadJugos(): int
# + obtenerCantidadVinosBlancos(): int
# + obtenerCantidadVinosTintosJovenes(): int
# + obtenerCantidadVinosTintosAnejados(): int

# Notas / Aclaraciones:
# - Cada vez que se repone un producto, se llena en su capacidad máxima.
# - Si la cantidad en depósito no es suficiente, se vende lo que se puede.


class Vinoteca:

    __capacidadMaxima = 5000

    def __init__(
        self,
        cantJugos: int = __capacidadMaxima,
        cantBlancos: int = __capacidadMaxima,
        cantTintosJovenes: int = __capacidadMaxima,
        cantTintosAnejados: int = __capacidadMaxima,
    ):
        self.__cantJugos = cantJugos
        self.__cantBlancos = cantBlancos
        self.__cantTintosJovenes = cantTintosJovenes
        self.__cantTintosAnejados = cantTintosAnejados

    def reponerJugos(self):
        self.__cantJugos = Vinoteca.__capacidadMaxima

    def reponerVinosBlancos(self):
        self.__cantBlancos = Vinoteca.__capacidadMaxima

    def reponerVinosTintoJoven(self):
        self.__cantTintosJovenes = Vinoteca.__capacidadMaxima

    def reponerVinosTintoAnejado(self):
        self.__cantTintosAnejados = Vinoteca.__capacidadMaxima

    def venderJugos(self, unidades: int):
        if unidades <= self.__cantJugos:
            self.__cantJugos -= unidades
        else:
            print(
                f"No se pudo completar la venta de {unidades} jugos. Solo se vendieron {self.__cantJugos} jugos."
            )
            self.__cantJugos = 0

    def venderVinosBlancos(self, unidades: int):
        if unidades <= self.__cantBlancos:
            self.__cantBlancos -= unidades
        else:
            print(
                f"No se pudo completar la venta de {unidades} vinos blancos. Solo se vendieron {self.__cantBlancos} vinos blancos."
            )
            self.__cantBlancos = 0

    def venderVinosTintosJovenes(self, unidades: int):
        if unidades <= self.__cantTintosJovenes:
            self.__cantTintosJovenes -= unidades
        else:
            print(
                f"No se pudo completar la venta de {unidades} vinos tintos jóvenes. Solo se vendieron {self.__cantTintosJovenes} vinos tintos jóvenes."
            )
            self.__cantTintosJovenes = 0

    def venderVinosTintosAnejados(self, unidades: int):
        if unidades <= self.__cantTintosAnejados:
            self.__cantTintosAnejados -= unidades
        else:
            print(
                f"No se pudo completar la venta de {unidades} vinos tintos añejados. Solo se vendieron {self.__cantTintosAnejados} vinos tintos añejados."
            )
            self.__cantTintosAnejados = 0

    def obtenerCantidadJugos(self):
        return self.__cantJugos

    def obtenerCantidadVinosBlancos(self):
        return self.__cantBlancos

    def obtenerCantidadVinosTintosJovenes(self):
        return self.__cantTintosJovenes

    def obtenerCantidadVinosTintosAnejados(self):
        return self.__cantTintosAnejados
