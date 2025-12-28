class Vehiculo:                  # Superclase
    def __init__(self, marca):
        self.marca = marca

    def transporte(self):
        print(f"Su vehículo preferido son los {self.marca}.")


class Edicion(Vehiculo):         # Subclase
    def __init__(self, marca, modelo):
        super().__init__(marca)  # Hereda el atributo de la superclase
        self.modelo = modelo

    def version(self):
        print(f"{self.marca} {self.modelo}")


superclase = Vehiculo("BMW")
subclase = Edicion("BMW", "M3")

superclase.transporte()
subclase.version()