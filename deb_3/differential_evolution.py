from scipy.optimize import differential_evolution
from functions import deb3, db3_bounds
import time

print('Introduce el numero de dimensiones')
D = int(input())

start_time = time.time()

bounds = db3_bounds * D

# Aplicar el algoritmo genetico
result = differential_evolution(deb3, bounds, mutation=(0.1, 0.2), recombination=0.9)

end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprime el resultado
print("Solución óptima: ", result.x)
print("Valor de la función objetivo en la solución óptima: ", result.fun)
print("Número de iteraciones: ", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")