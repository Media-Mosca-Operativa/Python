#METODOS PARA TRABAJAR CON LISTAS 
#Append añade un elemento al final de la lista
compra = ["leche", "harina", "maicena"]
compra.append("huevos")
print(compra)

#Insert inserta un elemento en el indice indicado
compra.insert(1, "sal") 
print(compra)

#Remove elimina el primer elemento que coincida
compra.remove("leche")
print(compra)

#Pop elimina un elemento en un indice indicado
eliminado = compra.pop(0) 
print(eliminado)
print(compra)

#Count cuenta cuantas los elementos que aparecen
elementos = compra.count
print(elementos)

#Clear vacia la lista
compra.clear()
print(compra)

#Index obtiene el indice del primer elemento que coincida
compra = ["leche", "huevos", "harina", "maicena"]
indice = compra.index("huevos")
print(indice)

#Sort ordena la lista en orden ascendente
compra.sort() #Orden ascendente
print(compra)

#Reverse invierte el orden de la lista
compra.reverse()
print(compra)

#Copy hace una copia de la lista 
lista_copia = compra.copy()
print(lista_copia)

#Extend añade los elementos de otra lista
compra_supermercado = ["solomillo", "hamburguesa"]
compra_carniceria = ["t-bone", "pata negra"]
compra_carniceria.extend(compra_supermercado)
print(compra_supermercado)