# b. Escribir una clase tester para verificar los servicios de la clase Empleado
# utilizando el constructor con todos los parámetros. Esta verificación debe
# permitir al usuario ingresar los datos de un empleado (legajo, cantidad de
# horas trabajadas en el mes, y valor de la hora) y luego mostrar su legajo y el
# sueldo calculado.

from ej2_a_sueldo_empleados import Empleado


class testEmpleado2:

    @staticmethod
    def test_empleado():
        # Solicitar al usuario los datos del empleado
        legajo = int(input("Ingrese el legajo del empleado: "))
        cantHoras = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        valorHora = float(input("Ingrese el valor de la hora: "))

        # Crear un objeto de la clase Empleado utilizando el constructor con todos los parámetros
        empleado = Empleado(legajo, cantHoras, valorHora)

        # Obtener el legajo y el sueldo calculado
        legajo_obtenido = empleado.obtenerLegajo()
        sueldo_calculado = empleado.obtenerSueldo()

        # Mostrar los resultados
        print(f"Legajo del empleado: {legajo_obtenido}")
        print(f"Sueldo calculado: ${sueldo_calculado:.2f}")


if __name__ == "__main__":
    testEmpleado2.test_empleado()
