import numpy as np
from scipy.optimize import differential_evolution
import time

def devilliers_glasser(x):
    result = 0.0
    for i in range(1, 25):
        ti = 0.1 * (i - 1)
        yi = 60.137 * 1.371 ** ti * np.sin(3.112 * ti + 1.761)
        term = x[0] * abs(x[1]) ** ti * np.sin(x[2] * ti + x[3]) - yi
        result += term**2

    return result

start_time = time.time()

bounds = [(-500, 500)] * 4

# Aplicar el algoritmo genetico
result = differential_evolution(devilliers_glasser, bounds)

end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprime el resultado
print("Solución óptima: ", result.x)
print("Valor de la función objetivo en la solución óptima: ", result.fun)
print("Número de iteraciones: ", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")