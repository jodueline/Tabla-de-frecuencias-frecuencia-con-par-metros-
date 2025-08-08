import math

# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line

# Datos de la población
poblacion = [15,32,45,56,52,49,68,47,18,21,48,49,56,52,39,48,49,61,44,52, 38,52,55,58,62,58,48,56,38,48,47,52,37,64,29,55,38,29,62,49, 69,18,61,55,49,35,60,31,56,21,29,31,34]

# Ordenando Datos
poblacion_ordenada = sorted(poblacion)
print("Datos ordenados")
print(poblacion_ordenada)

# Mostrar los datos en una tabla de 5 filas x 10 columnas
print("Datos ordenados en una tabla de 5 filas x 10 columnas:")
for i in range(0, len(poblacion_ordenada), 10):  # Avanza en pasos de 10 para columnas
    fila = poblacion_ordenada[i:i+10]  # Selecciona los próximos 10 elementos
    print(" ".join(f"{num:2}" for num in fila))  # Imprime la fila con espacios entre números

# Sacando Número de Elementos
n = len(poblacion)
print(f"Número de Elementos (N): {n}")  

# Sacando Valores Máximos y Mínimos
Vm = poblacion_ordenada[0]
Vmx = poblacion_ordenada[-1]
print(f"Datos mínimos y máximos: Min: {Vm} Max: {Vmx}")

# Promedio (Media)
Suma_datos = sum(poblacion_ordenada)
Promedio = Suma_datos / n
print(f"El promedio (media) es: µ = {Promedio}")

# Mostrar la sumatoria
print(f"La sumatoria de los datos es: {Suma_datos}")

# Desviación Media y Varianza
print("\nCálculos de desviación media y varianza:")
Determinante = 0
Desviacion_Media = 0
Dispercion = 0

print("x   |x - µ | (X - µ)²")
for i in poblacion_ordenada:
    Determinante = i - Promedio
    Dispercion += Determinante**2
    print(f"{i:2}  | {Determinante: .2f}  | {Determinante**2 : .2f}")
    Desviacion_Media += abs(Determinante)  # Se toma el valor absoluto directamente

# Calcular Desviación Media
print(f"\nLa Sumatoria |x - µ| es: {Desviacion_Media}")
Desviacion_Media /= n
print(f"\nLa Desviación Media (Sumatoria |x - µ| / N) es: {Desviacion_Media}")

# Calcular Varianza Poblacional
Varianza = Dispercion / n
print(f"La sumatoria de (x-µ)² es: {Dispercion}")
print(f"La Varianza Poblacional es: {Varianza}")

# Calcular Desviación Estándar
Desviacion_Estandar = math.sqrt(Varianza)
print(f"La Desviación Estándar es: {Desviacion_Estandar}")


# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line