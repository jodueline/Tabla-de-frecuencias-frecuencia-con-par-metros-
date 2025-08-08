import math


# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line

# Datos de la población
poblacion = [100,100,105,130,140,170,150,178,180,200,310,500,190,190,270,360,630,700,200,300,380,700,705,750,360,400,710,800,850,800,900]
# Ordenando Datos
poblacion_ordenada = sorted(poblacion)
print("Datos ordenados")
print(poblacion_ordenada)

# Mostrar los datos en una tabla de 5 filas por 10 columnas
print("Datos ordenados en una tabla de 5 filas x 10 columnas:")
for i in range(0, len(poblacion_ordenada), 5):  # Avanza en pasos de 10
    fila = poblacion_ordenada[i:i+5]  # Selecciona los próximos 10 elementos
    print(" ".join(f"{num:2}" for num in fila))  # Imprime la fila con espacios entre números

# Sacando Número de Clases
n = len(poblacion)
k = int(input(f"Escriba el valor Definido de K: {math.sqrt(n)} | "))  # K debe ser entero, no hace falta convertir la longitud de la lista a entero.
print(f"Número de Elementos (N): {n}")  
print(f"Número de Clases (K): {k}")

# Sacando rangos (Límites)
Vm = poblacion_ordenada[0]
Vmx = poblacion_ordenada[-1]
print(f"Datos mínimos y máximos: Min: {Vm} Max: {Vmx}")

# Fórmula del Rango
w = (Vmx - Vm) / k
print(f"Valor de rango obtenido: {w}")

if w.is_integer():  # Corregido: `is_integer()` comprueba si w es un número entero.
    DDR = 1
else:
    w = float(input("Define el rango específico: "))
    DDR = float(input("Define la reducción del rango: "))

# Definiendo la lista de rangos
rangos = []

# Definiendo rangos (Límites)
# Para la primera clase
# Tomando el límite mínimo aumentando el rango nos da el límite superior
# El límite superior se convierte en el límite inferior de la nueva clase

# Definiendo rangos (Límites)
for i in range(k):
    Vlm = Vm + w
    Vlm = Vlm - DDR
    print(f"{i} {Vm:.3f} {Vlm:.3f}")  # Formatea con 3 decimales
    rangos.append((round(Vm, 3), round(Vlm, 3)))
    Vm = Vlm + DDR  # Corregido: Avanza al siguiente límite inferior

print("Los rangos se definieron de esta manera:")
print(rangos)

# Contador de números en cada rango
resultados = {}

for Lmi, Lmx in rangos:
    count = sum(1 for x in poblacion if Lmi <= x <= Lmx)
    resultados[f"LM={Lmi}, LMX={Lmx}"] = count

FAAC=0
FR=0.0
FRA=0.0

# Mostrar resultados
print("___________________|_frecuencia absoluta__|___relativa_____")
for rango, cantidad in resultados.items():
    FR=cantidad/n
    print(f"{rango}|{cantidad}| {FR:.3f} ")
    print("____________________________")
    FAAC=FAAC+cantidad
    FRA=FRA+FR
print("frecuencia absoluta acumulada: ", FAAC, "Frecuencia relativa acumulada:", FRA)


# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line