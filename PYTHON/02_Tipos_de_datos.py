#Numeros enteros (int)
i = 10
y = -5

#Numeros decimales (float)
temperatura_dia = 12.5
temperatura_noche = -7.5

#Numeros complejos (complex)
i = 2 + 8j

#Cadenas de texto (str)
nombre = "Fernando"
saludo = 'Hola, ¿Que tal estás?'

#Datos booleanos (bool)
licencia = True
es_hermano = False

#Listas (list), colección de elementos ordenada y mutable
ropa = ["abrigo", "zapatos", "pantalones", "camisa"]
lista_numerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_mixta = [1, "melon", 7.5, True]

#Tuplas (tuple), colección de elementos ordenada y inmutable
equipo = ("Xavi Puig", "Joan Montserrat", "Jordi Vallgorguina")
tupla_numerica = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla_mixta = (10, "Guido van Rossum", True, 2.5, "Python", False)

#Conjuntos (set), colecciones no ordenadas de elementos unicos
equipo = {"Xavi Puig", "Joan Montserrat", "Jordi Vallgorguina"}
conjunto_numerico = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
conjunto_mixto = {18, 2.5, "Guido van Rossum", True, False, "Mundo"}

#Diccionarios (dict), colección de pares claves:valor
persona = {"nombre":"Fernando", "edad":23, "ciudad":"Sevilla" }
viajes = {"Guadalajara": False, "Milano": True, "Paris": False, }

#Datos None, representan las variables en ausencia de un valor
i = None 

# COMPROBACIÓN DEL TIPO DE DATO CON "type()"
x = 5
y = 2.5
z = "Guido van Rossum"
a = True
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]         
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)                
conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}             
diccionario = {"Terrasa": 1, "Manresa": 2, "Vallgorguina": 3}   

print(type(x))
print("Comprobando tipo de dato", type(x))                       # <class 'int'>
print("Comprobando tipo de dato", type(y))                       # <class 'float'>
print("Comprobando tipo de dato", type(z))                       # <class 'str'>
print("Comprobando tipo de dato", type(a))                       # <class 'bool'>
print("Comprobando tipo de dato:", type(lista))                  # <class 'list'>
print("Comprobando tipo de dato:", type(tupla))                  # <class 'tuple'>
print("Comprobando tipo de dato:", type(conjunto))               # <class 'set'>
print("Comprobando tipo de dato:", type(diccionario))            # <class 'dict'>