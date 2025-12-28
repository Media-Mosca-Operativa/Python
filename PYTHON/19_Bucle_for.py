"""
|---------ESTRUCTURAS DE CONTROL-----------|
|----------------BUCLE FOR-----------------|
|------------------------------------------| 
|-for elemento in variable:----------------|
|------Bloque de código que se recorre-----|
|------------------------------------------|
""" 
#Recorre & imprime declarados en la variable
i = "Strings, numbers o colecciones"
for x in i:
    print(x) 
    
"""
|---------ESTRUCTURAS DE CONTROL-----------|
|------------BUCLE FOR (range)-------------|
|------------------------------------------| 
|-for in range(numero):--------------------|
|------Bloque de código que se recorre-----|
|------------------------------------------|
""" 
#Recorre & imprime los numeros declarados en (range) 
for x in range(20):  
    print(x)
    
"""
|---------ESTRUCTURAS DE CONTROL-----------|
|---BUCLE FOR (range)(start, stop, step)---|
|------------------------------------------| 
|-for in range(inicio:fin:salto):----------|
|------Bloque de código que se recorre-----|
|------------------------------------------|
"""
#Recorre & imprime los numeros declarados en (range)
#Indicando inicio fin y salto
for x in range(1, 10, 3):
    print(x)
    

    