#METODOS CON CADENAS
amanecer = "Café Latte" 

#Len obtiene la longitud de la cadena
print(len(amanecer))                #Imprime 10
#Upper convierte las minusculas en mayusculas
print(amanecer.upper())             #Imprime "CAFE LATTE"
#Lower convierte las mayusculas en minisculas
print(amanecer.lower())             #Imprime "cafe latte" 
#Starswith comprueba si la cadena comienda con una subcadena
print(amanecer.startswith("Café"))  #Imprime True
#Endswith comprueba si la cadena termina con una subcadena
print(amanecer.endswith("Latte"))   #Imprime True
#Isalnum comprueba si la cadena contiene caracteres alfanumericos
print(amanecer.isalnum())           #Imprime False
#Isalpha comprueba si la cadena contiene solo letras
print(amanecer.isalpha())           #Imprime False
#Replace reemplaza una subcadena por otra
print(amanecer.replace("Latte", "Expresso")) #Imprime "Café Expresso"
#Split divide la cadena en una lista de subcadenas
print(amanecer.split())             #Imprime ['Cafe', 'Latte']


#Capitalize convierte la primera leta en mayuscula
i = "hola caracola"
print(i.capitalize())            #Imprime "Hola caracola"
#title convierte la primera letra de cada letra en mayuscula
print(i.title())  

#Strip elimina espacios al principio y al final
i = "   Hola Caracola   "
print(i.strip())                 #Imprime "Hola Caracola"

#Find busca la posicion de una subcadena dentro de la cadena
i = "Hola Caracola"
posicion = i.find("Caracola")    #Imprime 5 
print(posicion) 

#Count cuenta cuandas veces aparece una subcadena dentro de una cadena
i = "Hola Hola Hola Hola Hola Hola Hola Hola Hola  Hola"
contador = i.count("Hola")       #Imprime 10
print(contador)  
