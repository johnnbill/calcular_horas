import os
import readline

def pedir_hora(mensaje):
    hora = input(mensaje)

    if len(hora) == 4 and hora.isdigit():
        return f"{hora[:2]}:{hora[2:]}"

    else:
        print("Formato inválido")
        return pedir_hora(mensaje)

def calcular_tiempo_superado():
    total_tiempo_superado = 0

    while True:

        #os.system('clear')

        print("[1] Calcular tiempo")
        print("[2] Salir")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            hora_inicio = pedir_hora("Ingrese hora de inicio: ")
            hora_fin = pedir_hora("Ingrese hora de salida: ")

            #Convertimos las horas a minutos
            inicio_minutos = int(hora_inicio.split(":")[0]) * 60 + int(hora_inicio.split(":")[1])
            fin_minutos = int(hora_fin.split(":")[0]) * 60 + int(hora_fin.split(":")[1])

            diferencia_minutos = fin_minutos - inicio_minutos

            #Tiempo superado de 3 horas
            tiempo_superado = max(diferencia_minutos - 180, 0)

            total_tiempo_superado += tiempo_superado

            print("\n")
            print(f"Tiempo Adicional: {tiempo_superado // 60} horas y {tiempo_superado % 60} minutos")
            print(f"Tiempo Adicional Total: {total_tiempo_superado //60} horas y {total_tiempo_superado % 60} minutos")
            print("\n")

        elif opcion == "2":
            print("Hasta la proxima")
            break

calcular_tiempo_superado()
