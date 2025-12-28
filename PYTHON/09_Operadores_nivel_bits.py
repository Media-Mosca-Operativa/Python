"""
||--------------------------------------||
||--------OPERADORES NIVEL BITS---------||
||--------------------------------------||
||----------AND en binario "&"----------||
||-----------OR en binario "|"----------||
||----------XOR en binario "^"----------||
||----------NOT en binario "~"----------||
||--Desplazamiento a la izquiera "<<"---||
||--Desplazamiento a la derecha  ">>"---||
||--------------------------------------||
||----------1 BYTE = 8 BITS-------------||
||--------------0000 0000---------------||
||-|128|-|64|-|32|-|16|-|8|-|4|-|2|-|1|-||
||----------Conversión decimal----------||
||--|0|--|0|--|0|--|0|--|0|-|0|-|0|-|0|-||
||--------------------------------------||
||------------LOGICA BINARIA------------||
||--------------------------------------||
||---AND 1 & 1 = 1--|||--XOR 1 & 1 = 0--||
||---AND 1 & 0 = 0--|||--XOR 1 & 0 = 1--||
||---AND 0 & 1 = 0--|||--XOR 0 & 1 = 1--||
||---AND 0 & 0 = 0--|||--XOR 0 & 0 = 0--||
||------------------|||-----------------||
||----OR 1 & 1 = 1--|||-----------------||
||----OR 1 & 0 = 1--|||---NOT 1 = 0-----||
||----OR 0 & 1 = 1--|||---NOT 0 = 1-----||
||--------------------------------------||
"""
i = 8  # 1000 en binario
y = 9  # 1001 en binario

#Operador AND 
resultado = i & y
print(resultado)    # Imprime 8 (1000 en binario)

#Operador OR
resultado = i | y
print(resultado)    # Imprime  9 (1001 en binario)

#Operador XOR
resultado = i ^ y
print(resultado)    # Imprime  1 (0001 en binario)

#Operador NOT
resultado = ~i
print(resultado)    # Imprime  -9 (-1001 en binario)

#Desplazamiento a la izquiera <<
resultado = i << 1  # Desplazar 1 posición a la izquierda
print(resultado)    # Imprime  16 (0001 0000 en binario)

#Desplazamiento a la derecha >>
resultado = i >> 1  # Desplazar 1 posición a la derecha
print(resultado)    # Imprime  4 (0100 en binario)