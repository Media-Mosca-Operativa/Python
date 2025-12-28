"""
|------------------------ESTRUCTURAS DE CONTROL---------------------------|
|-------------------------SENTENCIAS DE CONTROL---------------------------|
|-------------------------------------------------------------------------|
|-------------------------------(break)-----------------------------------|
|------------------------------(continue)---------------------------------|
|--------------------------------(pass)-----------------------------------|
|-------------------------------(assert)----------------------------------|
|-------------------------------------------------------------------------|
"""
#Sentencia (break)
for i in range(20):
    if i == 10:
        break      # Interrumpe el bucle al llegar a la condición
    print("Break interrumple el contador del bucle", i)
    
#Sentencia (Continue)
for i in range(1, 10):
    if i == 5:
        continue   # Continua el bucle saltando el paso indicado
    print("Continue salta el paso indicado", i)


#Sentencia de control (pass)
if True:
    pass           # Define un bloque de codigo incompleto

#Sentencia de control (assert)    
x = 10
assert x == 10  

assert x > 10      # Condición nula AssertionError 
