import math

# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line


# Datos de la población
poblacion = [83,65,44,38,91,51,87,55,88,71,66,68,78,76,83,61,64,69,99,80, 82,51,98,84,68,65,70,67,47,65,54,75,82,60,51,56,66,77,42,56, 92,74, 79,66,73,60,68,62,74,55]
# Ordenando Datos

poblacion_ordenada = sorted(poblacion)
print("Datos ordenados")
print(poblacion_ordenada)

# Mostrar los datos en una tabla de 5 filas por 10 columnas

print("Datos ordenados en una tabla de 5 filas x 10 columnas:")
for i in range(0, len(poblacion_ordenada), 5):  # Avanza en pasos de 10
    fila = poblacion_ordenada[i:i+5]  # Selecciona los próximos 10 elementos
    print(" ".join(f"{num:2}" for num in fila))  # Imprime la fila con espacios entre números

# Sacando Número de Elementos
n = len(poblacion)
print(f"Número de Elementos (N): {n}")  

# Sacando Valores Max y Min
Vm = poblacion_ordenada[0]
Vmx = poblacion_ordenada[-1]
print(f"Datos mínimos y máximos: Min: {Vm} Max: {Vmx}")

#Promedio
Suma_datos=0
for i in poblacion_ordenada:
    Suma_datos=Suma_datos+ i
Promedio = Suma_datos/n

Promedio=float(input(f"El promedio es: µ ={Promedio}: "))
print(f" La sumatoria de x es = {Suma_datos}")

#desviacion poblacional

# Declaramos variables
Determiante = 0
Desviacion_Media= 0
Valor_adsoluto = 0
Dispercion=0

print("x   |x - µ | (X - µ)²")
for i in poblacion_ordenada:
    Determiante = i - Promedio
    Dispercion=Dispercion + (Determiante**2)
    print(f"{i}  | {Determiante: .2f}  | {Determiante*Determiante : .2f}  ")
    if  Determiante < 0 : 
        Determiante= Determiante * Determiante
        Determiante= math.sqrt(Determiante)
    Desviacion_Media= Desviacion_Media + Determiante

print(f"sumatoria |x- µ| = {Desviacion_Media}")

Desviacion_Media = Desviacion_Media/n
print("La Desviacion Media (Sumatoria / N) es:", Desviacion_Media)
print(f"La Sumatoria para la Varianza poblacinal es (x-µ)²: {Dispercion}")
print(f"La Varianza es : {Dispercion/n}")
print(f"La Desviacion estandar : ", math.sqrt(Dispercion/n))

# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line