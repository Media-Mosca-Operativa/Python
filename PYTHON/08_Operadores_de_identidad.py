"""
||---------------------------------------------------------------------||
||-------------------------OPERADORES DE IDENTIDAD---------------------||
||---------------------------------------------------------------------||
||-----IS-Compara dos coleciones si es el mismo objeto en memoria------||
||-IS NOT-Compara dos colecciones si NO son el mismo objeto en memoria-||
||---------------------------------------------------------------------||
"""
p = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Operador "IS"
print(p is t)  #Imprime False
print(p == t)  #Imprime True, diferencia igualdad
print(p is p)  #Imprime True

#Operador "IS NOT"
print(p is not t)  #Imprime True
print(p is not p)  #Imprime False
