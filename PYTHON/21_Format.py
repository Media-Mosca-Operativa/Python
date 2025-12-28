"""
||----------------------------------------|| 
||------------FORMATEAR STRINGS-----------||
||----------------------------------------||
||------"string {}".format(variable)------||
||----------------------------------------||
"""
#Ejemplo basico de "format()"
parametro = "Python"
variable = "Format asigna parametros no descritos. {}".format(parametro)
print(variable)

#Definiendo numeros decimales
decimales = 1.1998
variable = ".f Imprime la cantidad de decimales {:.2f}".format(decimales)
print(variable)

#Asignación de porcentajes
numero = 0.752018
variable =  "Asigna un porcentaje y inicio de este {:.2%}".format(numero)
print(variable)

#Muestra el signo si es positivo
numero = 10
variable = "El número es {:+d}".format(numero) 
print(variable)

numero = 10
variable = "El número es {: d}".format(numero) #Deja el espacio en blanco
print(variable)

#Puntear miles
numero = 1000000
variable = "Es posible puntear los miles {:,}".format(numero)
print(variable)

#Alineacion y ancho de campo
campo = "ancho"
ancho = "Alinea:{1:<15} izq, Alinea : {1:>15} der".format(campo, campo)
print(ancho)
