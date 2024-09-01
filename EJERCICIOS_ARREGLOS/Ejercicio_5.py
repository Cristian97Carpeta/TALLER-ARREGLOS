# Ejercicio 5: Invertir una lista

# Dada una lista, inviértela y crea una nueva lista con los elementos invertidos.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# SOLUCIÓN_1

numeros.reverse()

print(numeros)

print("----------------------------------------------------------------")

#SOLUCIÓN_2

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_invertidos = numeros[::-1] #se utiliza slicing para invertir la lista

print(numeros_invertidos)