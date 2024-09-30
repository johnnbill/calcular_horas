from datetime import datetime, timedelta

class Voluntariado:
    def __init__(self):
        self.horas_acumuladas = timedelta(0)
        self.horas_adicionales = timedelta(0)

    def registrar_horas(self, inicio, fin):
        delta = fin - inicio
        self.horas_acumuladas += delta
        self.horas_adicionales += max(delta - timedelta(hours=3), timedelta(0))

    def imprimir_resumen(self):
        print(f"Horas acumuladas: {self.horas_acumuladas}")
        print(f"Horas adicionales: {self.horas_adicionales}")


def main():
    voluntariado = Voluntariado()

    while True:
        print("\nOpción 1: Registrar horas")
        print("Opción 2: Imprimir resumen")
        print("Opción 3: Salir")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            inicio = input("Ingrese hora de inicio (HH:MM AM/PM): ")
            fin = input("Ingrese hora de fin (HH:MM AM/PM): ")
            
            inicio_dt = datetime.strptime(inicio, "%I:%M %p")
            fin_dt = datetime.strptime(fin, "%I:%M %p")
            
            # Asumir que si la hora de fin es antes que la hora de inicio, es del día siguiente
            if fin_dt < inicio_dt:
                fin_dt += timedelta(days=1)
            
            voluntariado.registrar_horas(inicio_dt, fin_dt)

        elif opcion == "2":
            voluntariado.imprimir_resumen()

        elif opcion == "3":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
