#METODOS CON DICCIONARIOS
#Get imprime el valor de una clave especifica
diccionario = {"nombre": "Fernando", "edad": 30}
valor = diccionario.get("nombre")
print(valor)

#Keys imprime las llaves del diccionario
claves = diccionario.keys()
print(claves)

#Values  imprime los valores del diccionario
valores = diccionario.values()
print(valores)

#Items imprime los pares del diccionario
pares = diccionario.items()
print(pares)

#Clear vacia el dicionario por completo
diccionario.clear()
print(diccionario)

#Pop elemina un valor especifico del diccionario
diccionario = {"nombre": "Fernando", "edad": 30}
valor = diccionario.pop("edad")
print(valor)
print(diccionario)

#Popitem elimina el ultimo par del diccionario
diccionario = {"nombre": "Fernando", "edad": 30}
ultimo_item = diccionario.popitem()
print(ultimo_item)
print(diccionario)

#Update actualiza el diccionario
diccionario = {"nombre": "Fernando", "edad": 30}
diccionario.update({"nombre": "Gerardo", "edad":35})
print(diccionario)

#Setdefault busca el item en el diccionario y si no lo encuentra lo agrega
diccionario = {"nombre": "Fernando", "edad": 30}
valor = diccionario.setdefault("Paris", False)
print(valor)
print(diccionario)

#Fromkeys crea un dicionario añadiendole unos valores
claves = ["Clave_1", "Clave_2", "Clave_3"]
diccionario = dict.fromkeys(claves, "Valor_general")
print(diccionario)