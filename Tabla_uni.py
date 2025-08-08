
# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line

import math
# Datos de la población
poblacion = [83,65,44,38,91,51,87,55,88,71,66,68,78,76,83,61,64,69,99,80, 82,51,98,84,68,65,70,67,47,65,54,75,82,60,51,56,66,77,42,56, 92,74, 79,66,73,60,68,62,74,55]

#Ordenando Datos
poblacion_ordenada = sorted(poblacion)

#Sacando Numero de Clases
#   ___
#K=V n  == N-clases
n=int(len(poblacion))
k = int(math.floor(math.sqrt(n)))
print(f"Numero de Elementos (N): {n}")
print(f"Numero de Clases (K): {k} ")

#Sacando rangos (Limites)
Vm=poblacion_ordenada[0]
Vmx=poblacion_ordenada[-1]
print(f"Datos minimos y maximos: Min: {Vm} Max {Vmx}")
#Formula del Rango
w=(Vmx-Vm)/k
print(f"Valor de rango optenido: {w}")
if w == int:
	print(":D")
	DDR=0.1
else:
	w=float(input("Define el rango espesifico: "))
	DDR=float(input("Define la reduccion del rango: "))


#Definiedo la lista de rangos
rangos = []

#Definiedo rangos (Limites)
#Para la primera clase
#Tomando el limite minimo aumentando el rango nos da el limite superior, Ahora
#El limite superior se convierte en el limite inferior de la nueva clase Vmin + W = LS 
#Repitiendo el cliclo hasta completas el total de clases (K)

for i in range(k) :
	Vlm=Vm+w
	Vlm=Vlm-DDR
	print(i,Vm,Vlm)
	rangos.append((Vm,Vlm))
	Vm=Vm+w

print(f"Los rangos se definieron de esta manera:")
print(rangos)
	


# Contador de números en cada rango
resultados = {}

for Lmi, Lmx in rangos:
	count = sum(1 for x in poblacion if Lmi <= x <= Lmx)
	resultados[f"LM={Lmi}, LMX={Lmx}"] = count

# Mostrar resultados
for rango, cantidad in resultados.items():
	 print(f"{rango}: {cantidad} números dentro del rango")


# Erick Josue Perez 
# @Yaret_hanns instagram 
# Jodue_line