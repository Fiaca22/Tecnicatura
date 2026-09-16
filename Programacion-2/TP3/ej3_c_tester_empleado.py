# c. Escribir otra clase tester para verificar los servicios de la clase Empleado.
# Esta verificación debe permitir al usuario ingresar los datos de un empleado
# (legajo, cantidad de horas trabajadas en el mes, y valor de la hora), crear el
# objeto empleado utilizando el constructor con el parámetro legajo, y luego
# modificar los demás atributos del objeto con los servicios provistos por la
# clase. Finalmente debe mostrar por pantalla el legajo y el sueldo del
# empleado.

from ej2_a_sueldo_empleados import Empleado


class testEmpleado3:

    @staticmethod
    def test_empleado():
        # Solicitar al usuario los datos del empleado
        legajo = int(input("Ingrese el legajo del empleado: "))
        cantHoras = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
        valorHora = float(input("Ingrese el valor de la hora: "))

        # Crear un objeto de la clase Empleado utilizando el constructor con el parámetro legajo
        empleado = Empleado(legajo)

        # Modificar los atributos del objeto utilizando los servicios provistos por la clase
        empleado.establecerHorasTrabajadas(cantHoras)
        empleado.establecerValorHora(valorHora)

        # Obtener el legajo y el sueldo calculado
        legajo_obtenido = empleado.obtenerLegajo()
        sueldo_calculado = empleado.obtenerSueldo()

        # Mostrar los resultados
        print(f"Legajo del empleado: {legajo_obtenido}")
        print(f"Sueldo calculado: ${sueldo_calculado:.2f}")


if __name__ == "__main__":
    testEmpleado3.test_empleado()
