# Una organización desea mantener información básica sobre sus empleados para
# calcular los sueldos, para ello diseñó la siguiente clase:
# a. implementar en python la clase Empleado.
# b. Escribir una clase tester para verificar los servicios de la clase Empleado
# utilizando el constructor con todos los parámetros. Esta verificación debe
# permitir al usuario ingresar los datos de un empleado (legajo, cantidad de
# horas trabajadas en el mes, y valor de la hora) y luego mostrar su legajo y el
# sueldo calculado.
# c. Escribir otra clase tester para verificar los servicios de la clase Empleado.
# Esta verificación debe permitir al usuario ingresar los datos de un empleado
# (legajo, cantidad de horas trabajadas en el mes, y valor de la hora), crear el
# objeto empleado utilizando el constructor con el parámetro legajo, y luego
# modificar los demás atributos del objeto con los servicios provistos por la
# clase. Finalmente debe mostrar por pantalla el legajo y el sueldo del
# empleado.

# Empleado
# <<atributos de instancia>>
# legajo: int
# horasTrabajadasMes: float
# valorHora: float

# <<constructores>>
# Empleado(legajo: int)
# Empleado(legajo: int, cantHoras: int, valorHora: float)

# <<comandos>>
# establecerHorasTrabajadas(cantHoras: int)
# establecerValorHora(valorHora: float)

# <<<consultas>>>
# obtenerLegajo() : int
# obtenerHorasTrabajadas() : int
# obtenerValorHora() : float
# obtenerSueldo() : float

# obtenerSueldo() : float
# devuelve el resultado de multiplicar la cantidad de horas
# trabajadas por el valor de cada hora.


class Empleado:

    __legajo = 0
    __horasTrabajadasMes = 0.0
    __valorHora = 0.0

    def __init__(self, legajo: int, cantHoras: int = 0, valorHora: float = 0.0):

        if not isinstance(legajo, int):
            raise TypeError("El legajo debe ser un número entero.")
        if not isinstance(cantHoras, int):
            raise TypeError(
                "La cantidad de horas trabajadas debe ser un número entero."
            )
        if not isinstance(valorHora, (int, float)):
            raise TypeError("El valor de la hora debe ser un número.")

        self.__legajo = legajo
        self.__horasTrabajadasMes = cantHoras
        self.__valorHora = valorHora

    def establecerHorasTrabajadas(self, cantHoras: int):
        if not isinstance(cantHoras, int):
            raise TypeError(
                "La cantidad de horas trabajadas debe ser un número entero."
            )
        self.__horasTrabajadasMes = cantHoras

    def establecerValorHora(self, valorHora: float):
        if not isinstance(valorHora, float):
            raise TypeError("El valor de la hora debe ser un número.")
        self.__valorHora = valorHora

    def obtenerLegajo(self):
        return self.__legajo

    def obtenerHorasTrabajadas(self):
        return self.__horasTrabajadasMes

    def obtenerValorHora(self):
        return self.__valorHora

    def obtenerSueldo(self):
        return self.__horasTrabajadasMes * self.__valorHora
