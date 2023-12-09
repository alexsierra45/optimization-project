import numpy as np
from scipy.optimize import minimize
import time

# Definición de la función objetivo
def objective_function(x):
    return -np.sum(np.sin(5 * np.pi * (abs(x)**(3/4) - 0.05))**6) / len(x)

print('Introduce el numero de dimensiones')
D = int(input())

start_time = time.time()

# Restricciones de desigualdad
bounds = [(-1, 1) for _ in range(D)]

# Punto de inicio para la optimización
initial_guess = np.random.uniform(low=-1, high=1, size=D)

# Función para la optimización con el método BFGS
result = minimize(objective_function, initial_guess, method='BFGS', bounds=bounds)

end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprimir resultados
print("Resultado de la optimización:")
print("Valor óptimo de la función:", result.fun)
print("Número de iteraciones:", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")
print("Punto óptimo:", result.x)