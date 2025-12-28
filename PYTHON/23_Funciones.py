""" 
|---------------------------------------|
|---------------FUNCIONES---------------|
|---------------------------------------|
|-def nombre_de_la_funcion(parametros):-|
|---Bloque de código que ejecuta--------|
|---return valor------------------------|
|-Llamada a la función------------------|
|---------------------------------------|
"""
def funcion(parametro):
    return "Así funcionan las", parametro

variable = funcion("funciones")
print(variable)

#Función con parametro predefinido
def funcion_parametros(x = "parametro predefinido"):
    print(f"Puedes llamar a la función con {x}!")

funcion_parametros()     # Llamada parametro predefinido
funcion_parametros("asignando parametro")   # Llamada parametro asignado

#Funciones lambda
variable = lambda p, t : p + t # Parametros
print(variable(8, 2)) # Valores

#Función con argumentos (*args)
def funcion(*args):
    valor = 0
    for sumar in args:
        valor += sumar # Orden a seguir
    return valor

print(funcion(5, 2, 3)) # Asignación de argumentos
print(funcion(5, 1, 2, 2))



