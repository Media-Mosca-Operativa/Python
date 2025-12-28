class Copia:
    def copyright(self):
        print("Infórmate del Copyright antes de nada...")

class Gerardo(Copia):
    def copyright(self):
        print("Dificil solución")

class Jesulin(Copia):
    def copyright(self):
        print("Es mi función")


c = Copia()
g = Gerardo()
j = Jesulin()

g.copyright()