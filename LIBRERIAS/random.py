import random

lista_1 = ["Red", "Green", "Blue"]
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

con_parametros = random.randint(1, 10)     # Numero aleatorio parametros (inicio, fin)
con_listas = random.choice(lista_1)        # Elemento aleatorio de una lista
random.shuffle(lista_2)                    # Mezcla elementos de la lista

print(con_parametros)
print(con_listas)
print(lista_2)

