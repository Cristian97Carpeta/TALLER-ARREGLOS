#Ejercicio 4: Eliminar duplicados

#Dada una lista con elementos duplicados, elimina los duplicados y crea una nueva lista con los elementos únicos.

lenguajes = ['python', 'java', 'ruby', 'php', 'javascript', 'html', 'css', 'python', 'c', 'java', 'python', 'java', 'ruby', 'php', 'javascript', 'html', 'css', 'python', 'c', 'java', 'rust', 'go', 'c', 'c++', 'c#', 'c', 'java', 'ruby', 'php', 'javascript', 'html', 'css', 'python', 'c', 'java', 'python', 'java', 'ruby', 'php', 'javascript', 'html', 'css', 'python', 'c', 'java', 'rust', 'go', 'c', 'c++', 'c#', 'c', 'java', 'ruby', 'php', 'javascript', 'html', 'css', 'python', 'c', 'java']

# SOLUCIÓN_1

lenguajes2 = list(set(lenguajes))

print("Lenguajes sin duplicados:", lenguajes2)


# SOLUCIÓN_2

lenguajes_unicos = []

# Recorrer la lista original
for lenguaje in lenguajes:
    if lenguaje not in lenguajes_unicos:
        lenguajes_unicos.append(lenguaje)

print(lenguajes_unicos)