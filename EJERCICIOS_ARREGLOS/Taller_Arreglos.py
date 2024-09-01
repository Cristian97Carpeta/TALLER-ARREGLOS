# EJERCICIO 1: Números pares e impares

# Dada una lista de números, crea dos listas separadas: una para los números pares y otra para los números impares.

#SOLUCION_1

numeros = range(100)
# se inicializa las listas para los numeros pares e impares
num_par: list [int] = []
num_impar: list [int] = []

for num in numeros: # se usa un for para iterar cada numero en el range
    if num % 2 == 0: # si el número es par, lo agrega a la lista de pares
        num_par.append(num)

    else: # si el número es impar lo agrega a la lista de impares
        num_impar.append(num)
print(num_par)
print(num_impar)
print("----------------------------------------------------------------")


#SOLUCION_2

numeros = range(100)

num_par = [num for num in numeros if num % 2 == 0] # se usa una comprencion de listas para crear una lista de números pares
num_impar = [num for num in numeros if num % 2 != 0] # se usa una comprensión de listas para crear una lista de números impares

print(num_par)
print(num_impar)





