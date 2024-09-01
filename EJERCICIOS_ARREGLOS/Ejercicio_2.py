# Ejercicio 2: Contador de vocales

# Dada una cadena de texto, cuenta cuántas veces aparece cada vocal (a, e, i, o, u) en el texto.

texto = 'Dada una cadena de texto, cuenta cuántas veces aparece cada vocal (a, e, i, o, u) en el texto.'

#SOLUCION_1

def contador_vocales (cad):
    vocales = "aeiouAEIOU"
    contador = [0,0,0,0,0]

for c in texto: # itera cada carácter de la cadena de texto
    for v in vocales:
        
    if v == c:
        if v == "a": # se incrementa el contador
            contador[0] += 1
        if v == "e":
            contador[1] += 1
        if v == "i":
            contador[2] += 1
        if v == "o":
            contador[3] += 1
        if v == "u":
            contador[4] += 1
    return contador # retorna la lista de contenedores


print(contador_vocales(texto))

print("----------------------------------------------------------------")

#SOLUCION_2

def contador_vocales(cad):
    vocales = "aeiouAEIOU"
    contador = {v: 0 for v in "aeiou"}

    for c in cad: # se itera cada carácter en la cadena
        if c in vocales:
            contador[c.lower()] += 1 # aquí se incrementa el contador correspondiente en minúscula

    return [contador[v] for v in "aeiou"] # retorna la lista con las vocales en orden

print(contador_vocales(texto))
