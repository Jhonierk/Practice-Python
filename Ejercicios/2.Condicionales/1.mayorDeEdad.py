"""
Escribir un programa que pregunte al usuario su edad 
y muestre por pantalla si es mayor de edad o no.
"""

edad=int(input("Por favor digite su edad: "))

if edad < 18:
	print("Lo sentimos eres menor de edad")
elif edad >= 18:
	print("Eres adulto bienvenido")
else:
	print("Has digitado mal")