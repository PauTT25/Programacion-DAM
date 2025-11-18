import math
from datetime import datetime

#Entrada de datos

caballos = int(input("Caballos:"))
capacidad_por_cuadra = int(input("Capacidad por cuadras:"))
fecha = input("Introduce la fecha (YYYY-MM-DD):")

#Cálculos

cuadras_necesarias = math.ceil(caballos / capacidad_por_cuadra)

#Fechas 
fecha = datetime.strptime(fecha, "%Y-%m-%d").date()


año = fecha.year
mes = fecha.month
dia = fecha.day

weekday = fecha.weekday()
isoweekday = fecha.isoweekday()

#Aqui le estamos pidiendo que nos imprima los resultados finales en pantalla

print("---Resultados---")
print("Hoy estamos a:", fecha)
print("Estamos en el año:", año)
print("En el mes:", mes)
print("Y a dia:", dia)
print("weekday():", weekday)
print("isoweekday():", isoweekday)
print("Cuadras necesarias:", cuadras_necesarias)





