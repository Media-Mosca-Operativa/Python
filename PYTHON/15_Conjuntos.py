#METODOS PARA TRABAJAR CON CONJUNTOS
#Add añade un elemento
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto.add(1)
print(conjunto)

#Remove elimina un elemento
conjunto.remove(2)
print(conjunto)
""" 
Discard elimina un elemento
a diferencia de remove no causa error si el elemento no existe
"""
conjunto.discard(2)
print(conjunto)

""" 
Pop elimina un elemento aleatorio
a diferencia de las listas no es posible indezar el elemento a eleminar
"""
#Pop elimina un elemento aleatorio
elemento = conjunto.pop()
print(elemento)
print(conjunto)

#Clear limpia el conjunto dejandolo vacio
conjunto.clear()
print(conjunto)

#Copy copia el conjunto
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_copia = conjunto.copy()
print(conjunto_copia)

#Union une dos conjuntos
conjunto_1 = {1, 2, 3, 4, 5}
conjunto_2 = {6, 7, 8, 9, 10}
conjunto = conjunto_1.union(conjunto_2)
print(conjunto)

#Intersection devuelve los elementos comunes
conjunto_1 = {1, 2, 3, 4, 7, 8, 9}
conjunto_2 = {1, 3, 5, 6, 7, 9, 10}
comunes = conjunto_1.intersection(conjunto_2)
print(comunes)

#Diference devuelve los elementos que no son comunes
conjunto_1 = {1, 2, 3, 4, 7, 8, 9}
conjunto_2 = {1, 3, 5, 6, 7, 9, 10}
diferencia = conjunto_1.difference(conjunto_2)
print(diferencia)

#Symetric difference devuelve los elementos que no estan en comun
conjunto_1 = {1, 2, 3, 4, 7, 8, 9}
conjunto_2 = {1, 3, 5, 6, 7, 9, 10}
diferencia_simetrica = conjunto_1.symmetric_difference(conjunto_2)
print(diferencia_simetrica)