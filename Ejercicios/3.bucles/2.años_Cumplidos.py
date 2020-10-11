"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los 
años que ha cumplido (desde 1 hasta su edad).
"""

edad=int(input("Por favor digite su edad: "))

for i in range(1, edad):
	print("Usted ha cumplido: " + str(i))

print("y su edad actual es: " + str(edad))

"""
age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
"""