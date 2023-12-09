import numpy as np
from scipy.optimize import minimize
import time

def deckers_art(x):
    x1, x2 = x
    term1 = 10**5 * x1**2
    term2 = x2**2
    term3 = (x1**2 + x2**2)**2
    term4 = 10**(-5) * (x1**2 + x2**2)**4

    return term1 + term2 - term3 + term4

start_time = time.time()

# Restricciones de desigualdad
bounds = [(-20, 20), (-20, 20)]

# Punto de inicio para la optimización
initial_guess = np.random.uniform(low=-20, high=20, size=2)

# Función para la optimización con el método BFGS
result = minimize(deckers_art, initial_guess, method='BFGS', bounds=bounds)

end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprimir resultados
print("Resultado de la optimización:")
print("Valor óptimo de la función:", result.fun)
print("Número de iteraciones:", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")
print("Punto óptimo:", result.x)