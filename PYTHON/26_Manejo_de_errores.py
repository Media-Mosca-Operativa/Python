"""
TRY envuelve un codigo que puede generar error
EXCEPT ejecuta un bloque de codigo si try caura error
ELSE ejecuta un codigo si el bloque de try no da error
FINALLY ejecuta un bloque de codigo independientemente del resto de bloques
"""
try:
    entrada = float(input("¿A que hora estamos 10,30?: "))
    salida = "Es la hora"
    datos = salida + entrada

except ValueError:
    print("Value Error")
    
else:
    print("Son las", datos) 
    
finally:
    print("Finally se ejecuta independientemente de try, except")
