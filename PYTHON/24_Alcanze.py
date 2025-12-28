"""
|--------------------------------------------------|
|----------------------SCOPE-----------------------|
|--------------------------------------------------|
|-variable global----------------------------------|
|--------------------------------------------------|
|-def funcion_local():-----------------------------|
|---variable local---------------------------------|
|---i = 5------------------------------------------|
|---print("Dentro de la función local, x =", i)----|
|--------------------------------------------------|
"""
i = 10 # Variable global

def funcion_local():
    i = 5 # Variable local
    print("Dentro de la función local, x =", i)

def funcion_global():
    print("Dentro de la función global, x =", i)

funcion_local()   
funcion_global()  

print("Fuera de las funciones, x =", i)  

#NONLOCAL
def funcion_exterior():
    x = 5  
    
    def funcion_interior():
        nonlocal x  
        x += 1
        print("Dentro de la función interior, x =", x)
    
    funcion_interior()  
    print("Dentro de la función exterior, x =", x)

funcion_exterior()