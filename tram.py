import time
import random
import matplotlib.pyplot as plt

def capacidad_tranvia(n, paradas):
    pasajeros_actuales = 0
    capacidad_max = 0
    for ai, bi in paradas:
        pasajeros_actuales -= ai
        pasajeros_actuales += bi
        if pasajeros_actuales > capacidad_max:
            capacidad_max = pasajeros_actuales
    return capacidad_max

n_values = [100, 250, 500, 750, 1000]
tiempos = []

for n in n_values:
    tiempo_total = 0
    for _ in range(10):  
        paradas = []
        pasajeros = 0
        for i in range(n):
            ai = random.randint(0, pasajeros)
            bi = random.randint(50, 100)  
            paradas.append((ai, bi))
            pasajeros = pasajeros - ai + bi
        paradas[-1] = (pasajeros, 0)
        
        start = time.time()
        capacidad_tranvia(n, paradas)
        end = time.time()
        tiempo_total += (end - start) * 1000
    tiempos.append(tiempo_total / 10)  

plt.plot(n_values, tiempos, marker='o')
plt.title("Tiempo de ejecución vs número de paradas")
plt.xlabel("Número de paradas (n)")
plt.ylabel("Tiempo promedio (ms)")
plt.grid(True)
plt.show()
