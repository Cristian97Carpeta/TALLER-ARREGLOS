#Ejercicio 3: Calculadora de promedios

#Crea una lista de calificaciones y calcula el promedio de las calificaciones.

calificaciones = [
    [4, 4.3, 4.8, 5, 2, 4.9],
    [2, 3, 1.8, 2.5, 2.9, 5],
    [3, 0.3, 0.8, 5, 4.8, 5],
]


#SOLUCION_1

promedios = [] # se inicia una lista vacia para los promedios
cantidad= 0
suma= 0

for c in calificaciones: #se itera cada lista de calificaciones
    suma = 0
    cantidad = 0
    for n in c: # se itera sobre cada calificacion en la lista
        suma += n # se suma la calificacion actual a la suma total
        cantidad += 1 # incrementa en contador en las calificaciones
    promedios.append(suma/cantidad) # calcula el promedio y y lo agrega a la lista de promedis
print(promedios)

print("----------------------------------------------------------------")

#SOLUCIÓN_2


calificaciones = [
    [4, 4.3, 4.8, 5, 2, 4.9],
    [2, 3, 1.8, 2.5, 2.9, 5],
    [3, 0.3, 0.8, 5, 4.8, 5],
]


promedios = [] # se inicia una lista vacía para almacenar los promedios


for c in calificaciones:  # Itera sobre cada lista de calificaciones

    promedio = sum(c) / len(c)   # Calculamos el promedio de la lista actual y lo agregamos a la lista de promedios
    promedios.append(promedio)


print(promedios)
