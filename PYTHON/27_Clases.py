class Area:
    #Funcion iniciadora
    def __init__(self, i, x): #__init__ es un constructor que inicia los parametros
        self.i = i # Atributos de instancia
        self.x = x # Atributos de instancia

    def funcion(self):
        print(f"Algo extraño envuelve {self.i}, junto lo que {self.x} ahí.")

# Es posible crear varias instancias de una clase        
Objetos_1 = Area("el pueblo","hacen") 
Objetos_2 = Area("la provincia", "estudian")

Objetos_1.funcion() # Llamada a la función
Objetos_2.funcion() # Llamada a la función

""" 
|--------------------------------------------|
|----METODOS @classmethod & @staticmethod----|
|--------------------------------------------|
"""
class Diferencia:
    
    metodo = "de clase"
    
    @classmethod
    def clase(cls):
        return cls.metodo
    
    def __init__(self, tipo):
        self.tipo = tipo
        
    @staticmethod
    def estatico(tipo):
        print(f"Metodo {tipo}")
        
Diferencia.estatico("estatico")
print("Metodo", Diferencia.clase())

