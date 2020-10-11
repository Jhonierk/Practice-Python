"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
todos los números impares desde 1 hasta ese número separados por comas.
"""

num=int(input("Por favor digita un numero positivo: "))

print("numeros impares: ")

for i in range (1, num+1, 2):
	print(str(i), end=",")