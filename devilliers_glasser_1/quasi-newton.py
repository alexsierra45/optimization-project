import numpy as np
from scipy.optimize import minimize
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

# Restricciones de desigualdad
bounds = [(-500, 500) for _ in range(4)]

# Punto de inicio para la optimización
initial_guess = np.random.uniform(low=-500, high=500, size=4)

# Función para la optimización con el método BFGS
result = minimize(devilliers_glasser, initial_guess, method='BFGS', bounds=bounds)

end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprimir resultados
print("Resultado de la optimización:")
print("Valor óptimo de la función:", result.fun)
print("Número de iteraciones:", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")
print("Punto óptimo:", result.x)