class Microondas:

    def __init__(self):
        self.estado = "APAGADO"

    def abrir_puerta(self):
        if self.estado == "APAGADO" or self.estado == "LISTO":
            self.estado = "PUERTA_ABIERTA"
            print("Puerta abierta")
        else:
            print("No se puede abrir la puerta en este estado")

    def cerrar_puerta(self):
        if self.estado == "PUERTA_ABIERTA":
            self.estado = "LISTO"
            print("Puerta cerrada, listo para iniciar")
        else:
            print("La puerta ya está cerrada")

    def iniciar(self):
        if self.estado == "LISTO":
            self.estado = "COCINANDO"
            print("Microondas cocinando...")
        else:
            print("No se puede iniciar")

    def terminar(self):
        if self.estado == "COCINANDO":
            self.estado = "FINALIZADO"
            print("Cocción terminada")
        else:
            print("No se puede terminar")

    def reiniciar(self):
        if self.estado == "FINALIZADO":
            self.estado = "APAGADO"
            print("Microondas apagado")
        else:
            print("No se puede reiniciar")

    def estado_actual(self):
        print("Estado actual:", self.estado)


# Programa principal
micro = Microondas()

while True:
    print("\n----- MICROONDAS -----")
    print("1. Abrir puerta")
    print("2. Cerrar puerta")
    print("3. Iniciar cocción")
    print("4. Terminar cocción")
    print("5. Reiniciar")
    print("6. Ver estado")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        micro.abrir_puerta()

    elif opcion == "2":
        micro.cerrar_puerta()

    elif opcion == "3":
        micro.iniciar()

    elif opcion == "4":
        micro.terminar()

    elif opcion == "5":
        micro.reiniciar()

    elif opcion == "6":
        micro.estado_actual()

    elif opcion == "7":
        print("Programa terminado")
        break

    else:
        print("Opción inválida")