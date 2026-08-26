import json
import os

ARCHIVO_DATOS = "servidor_datos.json"


class PozoPC:
    def __init__(self):
        self.integrantes = []
        self.saldos = {}
        self.valor_pc = 0.0
        self.caja_efectivo = 0.0
        self.cargar_datos()

    def guardar_datos(self):
        datos = {
            "integrantes": self.integrantes,
            "saldos": self.saldos,
            "valor_pc": self.valor_pc,
            "caja_efectivo": self.caja_efectivo,
        }
        try:
            with open(ARCHIVO_DATOS, "w") as f:
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"\n[ERROR] No se pudieron guardar los datos: {e}")

    def cargar_datos(self):
        if os.path.exists(ARCHIVO_DATOS):
            try:
                with open(ARCHIVO_DATOS, "r") as f:
                    datos = json.load(f)
                    self.integrantes = datos.get("integrantes", [])
                    self.saldos = datos.get("saldos", {})
                    self.valor_pc = datos.get("valor_pc", 0.0)
                    self.caja_efectivo = datos.get("caja_efectivo", 0.0)
            except Exception:
                self.inicializar_vacio()
        else:
            self.inicializar_vacio()

    def inicializar_vacio(self):
        self.integrantes = []
        self.saldos = {}
        self.valor_pc = 0.0
        self.caja_efectivo = 0.0

    def inicializar_sociedad(self):
        print("\n=== CONFIGURACIÓN INICIAL DE LA SOCIEDAD ===")
        try:
            cant = int(input("¿Cuántos socios iniciales son?: "))
            if cant <= 0:
                print("Debe haber al menos 1 socio.")
                return

            nombres = []
            for i in range(cant):
                n = input(f"Nombre del socio {i+1}: ").strip().capitalize()
                if n and n not in nombres:
                    nombres.append(n)

            self.valor_pc = float(input("Valor inicial acordado de la PC (USD): "))

            cuota = self.valor_pc / len(nombres)
            self.integrantes = nombres
            self.saldos = {}
            self.caja_efectivo = 0.0

            print(
                f"\nValor total: ${self.valor_pc:.2f} USD | Cuota ideal ({(100/len(nombres)):.1f}%): ${cuota:.2f} USD c/u"
            )
            for nombre in nombres:
                monto = float(
                    input(f"¿Cuánto dinero/componentes puso {nombre} (USD)?: ")
                )
                self.saldos[nombre] = monto - cuota

            self.guardar_datos()
            print("\n[ÉXITO] Sociedad inicializada correctamente.")
        except ValueError:
            print("\n[ERROR] Entrada inválida. Ingrese valores numéricos adecuados.")

    def mostrar_estado(self):
        if not self.integrantes:
            print("\n[INFO] No hay una sociedad configurada actualmente.")
            return

        pct = 100.0 / len(self.integrantes)
        print("\n" + "=" * 50)
        print(f"=== ESTADO ACTUAL (PC Valuada en: ${self.valor_pc:.2f} USD) ===")
        print(f"Participación igualitaria: {pct:.1f}% cada uno")
        print(f"EFECTIVO DISPONIBLE EN CAJA: ${self.caja_efectivo:.2f} USD")
        print("=" * 50 + "\n")

        for socio in self.integrantes:
            saldo = self.saldos.get(socio, 0.0)
            if saldo > 0.001:
                retirable_hoy = min(saldo, self.caja_efectivo)
                estado = f"A FAVOR: +${saldo:.2f} USD | Puede retirar HOY: ${retirable_hoy:.2f} USD"
            elif saldo < -0.001:
                estado = f"EN DEUDA: -${abs(saldo):.2f} USD (debe depositar)"
            else:
                estado = "AL DÍA ($0.00 USD)"
            print(f"- {socio:<12} | {estado}")
        print("=" * 50)

    def movimiento_pozo(self):
        if not self.integrantes:
            print("\n[INFO] Configure la sociedad primero.")
            return

        print("\n--- MOVIMIENTO DE DINERO ---")
        print("1. Un socio deposita dinero para saldar deuda")
        print("2. Un socio retira dinero de su saldo a favor")

        opc = input("Seleccione (1-2): ").strip()
        if opc not in ["1", "2"]:
            print("Opción no válida.")
            return

        socio = self.seleccionar_socio()
        if not socio:
            return

        try:
            monto = float(input("Ingrese el monto (USD): "))
            if monto <= 0:
                print("El monto debe ser mayor a 0.")
                return

            if opc == "1":
                self.saldos[socio] += monto
                self.caja_efectivo += monto
                print(f"\n[ÉXITO] {socio} depositó ${monto:.2f} USD.")
                print(f"Efectivo en caja actualizado: ${self.caja_efectivo:.2f} USD.")
            else:
                retirable_max = min(self.saldos[socio], self.caja_efectivo)
                if monto > retirable_max:
                    print(f"\n[ERROR] No se pueden retirar ${monto:.2f} USD.")
                    print(
                        f"Límite actual: Tiene +${self.saldos[socio]:.2f} USD a favor, pero en caja solo hay ${self.caja_efectivo:.2f} USD disponibles."
                    )
                    return

                self.saldos[socio] -= monto
                self.caja_efectivo -= monto
                print(f"\n[ÉXITO] {socio} retiró ${monto:.2f} USD del pozo.")
                print(f"Efectivo en caja restante: ${self.caja_efectivo:.2f} USD.")

            self.guardar_datos()
        except ValueError:
            print("\n[ERROR] Debe ingresar un número válido.")

    def agregar_componente(self):
        if not self.integrantes:
            print("\n[INFO] Configure la sociedad primero.")
            return

        print("\n--- AGREGAR COMPONENTE / MANTENIMIENTO ---")
        nombre_comp = input("Nombre del componente/mantenimiento: ").strip()
        try:
            costo = float(input("Costo total en USD: "))
            if costo <= 0:
                print("El costo debe ser mayor a 0.")
                return

            print("¿Quién lo pagó de su bolsillo?")
            pagador = self.seleccionar_socio()
            if not pagador:
                return

            cuota = costo / len(self.integrantes)
            self.valor_pc += costo

            for s in self.integrantes:
                if s == pagador:
                    self.saldos[s] += costo - cuota
                else:
                    self.saldos[s] -= cuota

            self.guardar_datos()
            print(f"\n[ÉXITO] Componente '{nombre_comp}' agregado.")
            print(f"El valor total de la PC subió a ${self.valor_pc:.2f} USD.")
            print(
                f"A cada uno se le imputaron -${cuota:.2f} USD y a {pagador} +${(costo - cuota):.2f} USD."
            )
        except ValueError:
            print("\n[ERROR] Debe ingresar un valor numérico válido.")

    def gestionar_integrantes(self):
        if not self.integrantes:
            print("\n[INFO] Configure la sociedad primero.")
            return

        print("\n--- MODIFICAR INTEGRANTES ---")
        print("1. Ingresar nuevo socio")
        print("2. Retirar un socio")

        opc = input("Seleccione (1-2): ").strip()
        if opc == "1":
            nuevo = input("Nombre del nuevo integrante: ").strip().capitalize()
            if not nuevo or nuevo in self.integrantes:
                print("Nombre inválido o ya existente.")
                return

            try:
                monto = float(
                    input(f"¿Cuánto dinero aporta {nuevo} al entrar (USD)?: ")
                )
                num_viejos = len(self.integrantes)
                self.integrantes.append(nuevo)

                cuota_nueva = self.valor_pc / len(self.integrantes)
                cuota_vieja = self.valor_pc / num_viejos
                dif = cuota_vieja - cuota_nueva

                for s in self.integrantes:
                    if s == nuevo:
                        self.saldos[s] = monto - cuota_nueva
                        if self.saldos[s] > 0:
                            self.caja_efectivo += self.saldos[s]
                    else:
                        self.saldos[s] += dif

                self.guardar_datos()
                print(
                    f"\n[ÉXITO] {nuevo} ingresó a la sociedad. Ahora son {len(self.integrantes)} socios."
                )
            except ValueError:
                print("\n[ERROR] Valor numérico inválido.")

        elif opc == "2":
            socio_sale = self.seleccionar_socio()
            if not socio_sale:
                return

            try:
                val_actual = float(
                    input(
                        f"Valuación actual acordada del servidor (USD) [Actual: ${self.valor_pc:.2f}]: "
                    )
                )
                num_actual = len(self.integrantes)
                base = val_actual / num_actual
                saldo_s = self.saldos[socio_sale]
                a_pagar_total = base + saldo_s

                # Guardamos la lista de los socios que se quedan
                socios_quedan = [s for s in self.integrantes if s != socio_sale]
                num_restantes = len(socios_quedan)
                pago_por_persona = a_pagar_total / num_restantes

                # Aplicar cambios
                self.integrantes.remove(socio_sale)
                del self.saldos[socio_sale]

                for s in self.integrantes:
                    self.saldos[s] -= pago_por_persona

                self.valor_pc = val_actual
                self.guardar_datos()

                print("\n" + "=" * 50)
                print(f"=== LIQUIDACIÓN Y RETIRO DE {socio_sale.upper()} ===")
                print(
                    f"1. Valor de su parte en la PC ({(100/num_actual):.1f}%): ${base:.2f} USD"
                )
                if saldo_s >= 0:
                    print(f"2. Saldo a favor acumulado en pozo: +${saldo_s:.2f} USD")
                else:
                    print(f"2. Deuda previa en pozo: -${abs(saldo_s):.2f} USD")
                print(
                    f"-> TOTAL LIQUIDADO A PAGARLE A {socio_sale.upper()}: ${a_pagar_total:.2f} USD"
                )
                print("-" * 50)
                print("DESGLOSE DE PAGO DE LOS SOCIOS QUE SE QUEDAN:")
                for s in socios_quedan:
                    print(
                        f"-> {s} debe abonarle a {socio_sale}: ${pago_por_persona:.2f} USD"
                    )
                print("=" * 50)

            except ValueError:
                print("\n[ERROR] Valor numérico inválido.")

    def resetear_todo(self):
        print("\n" + "!" * 45)
        print("!!! ADVERTENCIA DE RESETEO TOTAL !!!")
        print("Esta acción borrará a todos los socios, saldos y datos guardados.")
        print("!" * 45)

        conf1 = input(
            "\n[PASO 1/3] Para continuar, escriba exactamente la palabra 'RESET': "
        ).strip()
        if conf1 != "RESET":
            print("\n[CANCELADO] Palabra clave incorrecta. No se modificó nada.")
            return

        conf2 = (
            input("[PASO 2/3] ¿Está seguro de eliminar TODOS los datos? (S/N): ")
            .strip()
            .upper()
        )
        if conf2 != "S":
            print("\n[CANCELADO] Operación abortada.")
            return

        conf3 = (
            input(
                "[PASO 3/3] Última confirmación. Ingrese 'SI' para confirmar el borrado definitivo: "
            )
            .strip()
            .upper()
        )
        if conf3 == "SI":
            self.inicializar_vacio()
            if os.path.exists(ARCHIVO_DATOS):
                try:
                    os.remove(ARCHIVO_DATOS)
                except Exception as e:
                    print(f"Error al eliminar el archivo: {e}")
            print("\n[SISTEMA RESETEADO] Todos los datos han sido borrados a 0.")
        else:
            print("\n[CANCELADO] Operación abortada en el último paso.")

    def seleccionar_socio(self):
        print("\nSeleccione un socio:")
        for idx, nombre in enumerate(self.integrantes, 1):
            print(f"{idx}. {nombre}")
        try:
            opc = int(input("Número de socio: "))
            if 1 <= opc <= len(self.integrantes):
                return self.integrantes[opc - 1]
            print("Número de socio fuera de rango.")
        except ValueError:
            print("Entrada no válida.")
        return None


def menu_principal():
    pozo = PozoPC()

    while True:
        print("\n" + "=" * 40)
        print("     GESTOR DE SERVIDOR Y POZO PC     ")
        print("=" * 40)
        print("1. Ver Estado de Cuentas y Porcentajes")
        print("2. Registrar Movimiento (Aportar / Retirar)")
        print("3. Agregar Componente o Mantenimiento")
        print("4. Modificar Sociedad (Entrada / Salida)")
        print("5. Configuración Inicial de la Sociedad")
        print("6. RESETEAR TODO A 0")
        print("7. Salir")
        print("=" * 40)

        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            pozo.mostrar_estado()
        elif opcion == "2":
            pozo.movimiento_pozo()
        elif opcion == "3":
            pozo.agregar_componente()
        elif opcion == "4":
            pozo.gestionar_integrantes()
        elif opcion == "5":
            if pozo.integrantes:
                res = (
                    input(
                        "Ya existe una sociedad registrada. ¿Desea reconfigurarla? (S/N): "
                    )
                    .strip()
                    .upper()
                )
                if res == "S":
                    pozo.inicializar_sociedad()
            else:
                pozo.inicializar_sociedad()
        elif opcion == "6":
            pozo.resetear_todo()
        elif opcion == "7":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n[!] Opción no válida. Por favor, ingrese un número del 1 al 7.")


if __name__ == "__main__":
    menu_principal()
