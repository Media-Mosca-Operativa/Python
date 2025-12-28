#OPERADORES RELACIONALES
"""
||-------------------------||
||-OPERADORES RELACIONALES-||
||-------------------------||
||------IGUALDAD (==)------||
||----DESIGUALDAD (!=)-----||
||------MAYOR QUE (>)------||
||------MENOR QUE (<)------||
||-MAYOR O IGUAL QUE  (>=)-||
||-MENOR O IGUAL QUE  (<=)-||
||-------------------------||
"""
q = 10
w = 20
e = 25
r = 15
t = 30
y = 20

#Operador de igualdad "=="
print(w == y)   #Imprime True
print(w == q)   #Imprime False

#Operador de desigualdad "!="
print(w != t)   #Imprime True
print(w != y)   #Imprime False

#Operador mayor que ">"
print(w > q)    #Imprime True
print(w > t)    #Imprime False

#Operarador menor que "<"
print(w < t)    #Imprime True
print(w < q)    #Imprime False

#Operador mayor o igual que ">="
print(w >= y)   #Imprime True
print(w >= t)   #Imprime False

#Operador menor o igual que "<="
print(w <= y)   #Imprime True
print(w <= q)   #Imprime False

#Combinaciones entre cadenas de texto strings
p = "Hola"
t = "Caracola"
print(p == t)   #Imprime False
print(p < t)    #Imprime False
print(p > t)    #Imprime True
print(p <= t)   #Imprime False
print(p >= t)   #Imprime True