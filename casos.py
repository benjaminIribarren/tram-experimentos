import os
import csv

def capacidad_tranvia(n, paradas):
    pasajeros_actuales = 0
    capacidad_max = 0
    for ai, bi in paradas:
        pasajeros_actuales -= ai
        pasajeros_actuales += bi
        capacidad_max = max(capacidad_max, pasajeros_actuales)
    return capacidad_max

nombre_archivo = input("Ingrese el nombre del archivo CSV (ej: caso_prueba_1.csv): ")

if not os.path.exists(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' no existe.")
else:
    with open(nombre_archivo, newline="") as f:
        reader = csv.reader(f)
        lineas = list(reader)

        try:
            n = int(lineas[0][0])
        except ValueError:
            print("El archivo no tiene un número de paradas válido en la primera línea.")
            exit() 

        paradas = []
        for i in range(1, len(lineas)):
            if len(lineas[i]) < 2:  
                print(f"Línea {i+1} no tiene dos valores.")
                exit()
            ai, bi = map(int, lineas[i])
            paradas.append((ai, bi))

        if len(paradas) != n:
            print(f"Se esperaban {n} paradas pero se leyeron {len(paradas)}.")
            exit() 

        # Paradas
        print("\nParadas leídas del archivo:")
        print("Parada\tBajan(ai)\tSuben(bi)")
        for idx, (ai, bi) in enumerate(paradas, 1):
            print(f"{idx}\t{ai}\t\t{bi}")

        # Capacidad mínima
        capacidad = capacidad_tranvia(n, paradas)
        print(f"\nCapacidad mínima necesaria del tranvía: {capacidad}")
