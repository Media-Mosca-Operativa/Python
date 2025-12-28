"""
||------------------------------------------------------------||
||------------------OPERADORES DE PERTENENCIA-----------------||
||------------------------------------------------------------||
||--------IN--Busca el elemento dentro de una colección-------||
||-NOT IN-busca el elemento y devuelve el valor invertido-----||
||------------------------------------------------------------||
"""
ropa = ["abrigo", "zapatos", "pantalones", "camisa"]

#Operador "IN"

print("abrigo" in ropa)  # Imprime True
print("smoking" in ropa)  # Imprime False

#Operador "NOT IN"

print("abrigo" not in ropa)  # Imprime False
print("smoking"  not in ropa)  # Imprime True
