from scipy.optimize import differential_evolution
import time

def deckers_art(x):
    x1, x2 = x
    term1 = 10**5 * x1**2
    term2 = x2**2
    term3 = (x1**2 + x2**2)**2
    term4 = 10**(-5) * (x1**2 + x2**2)**4

    return term1 + term2 - term3 + term4

start_time = time.time()

bounds = [(-20, 20)] * 2

# Aplicar el algoritmo genetico
result = differential_evolution(deckers_art, bounds)

end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprime el resultado
print("Solución óptima: ", result.x)
print("Valor de la función objetivo en la solución óptima: ", result.fun)
print("Número de iteraciones: ", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")