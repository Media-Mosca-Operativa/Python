"""
||-----------------------------------------------||
||-------------OPERADORES  LOGICOS---------------||
||-----------------------------------------------||
||--AND--Ambas expresiones tienen que coincidir--||
||-----OR--Una expresión tiene que coincidir-----||
||----------NOT--Invierte la expresión-----------||
||-----------------------------------------------||
"""
#Operador "AND"
resultado = (10 > 30) and (25 > 15)
print(resultado)  # Imprime False

#Operador "OR"
resultado = (25 > 20) or (15 < 20)
print(resultado)  # Imprime True

#Operador "NOT"
resultado = not (15 > 30)
print(resultado)  # Imprime False

q = 10
w = 20
e = 25
r = 15
t = 30
y = 20
#Operador "AND"
resultado = (q > t) and (e > r)
print(resultado)  # Imprime False

#Operador "OR"
resultado = (e > w) or (r < y)
print(resultado)  # Imprime True

#Operador "NOT"
resultado = not (e > q)
print(resultado)  # Imprime True
resultado = not (r > t)
print(resultado)  # Imprime False

# Combinamos operadores "and" y "or"
resultado = (q > t) and (e > r) or (r < y)
print(resultado)  # Imprime True
resultado = not (q > t) and (e > r) or (r < y)
print(resultado)  # Imprime False
