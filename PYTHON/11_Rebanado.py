"""
||----------------------------------------|| 
||------------REBANADO (slicing)----------||
||----------------------------------------||
||----print(elemento[inicio:fin:salto])---||
||---------print(elemento[1:10:1])--------||
||----------------------------------------||
"""

ropa = ["abrigo", "zapatos", "pantalones", "camisa"]
print(ropa[0:2])        # Imprime ['abrigo', 'zapatos']
print(ropa[::2])        # Imprime ['abrigo', 'pantalones']
print(ropa[1:3:2])      # Imprime ['zapatos']
print(ropa[-4:])        # Imprime ['zapatos', 'pantalones', 'camisa']
print(ropa[::-1])       # Imprime ['camisa', 'pantalones', 'zapatos', 'abrigo']

saludo = "Hola Caracola"
print(saludo[0:6:2])    # Hl
print(saludo[10:])      # Imprime ola
print(saludo[::-1])     # Imprime alocaraC aloH

