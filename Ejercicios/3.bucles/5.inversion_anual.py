"""
Escribir un programa que pregunte al usuario una cantidad a invertir, 
el interés anual y el número de años, y muestre por pantalla el capital obtenido 
en la inversión cada año que dura la inversión.
"""

monto=float(input("Digite cantidad a invertir: "))
interes=float(input("Digite el interes anual: "))
anio=int(input("Digite años: "))

for i in range(anio):
	monto *= 1+interes /100
	print("capital " + str(i+1) + " años: " + str(round(monto, 2)))