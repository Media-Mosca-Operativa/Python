from datetime import datetime

# Imprime fecha y hora actual
fecha_hora = datetime.now()
print(fecha_hora)


# Formatear datos a imprimir parametros "%d/%m/%Y %H:%M:%S"
fecha_formateada = fecha_hora.strftime("%d/%m/%Y %H:%M")
tiempo_local = fecha_hora.strftime("%c")

print("Formateado:", fecha_formateada)
print("Fecha local:", tiempo_local)