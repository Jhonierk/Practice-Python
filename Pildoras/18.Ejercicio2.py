"""
Crea un programa que pida números positivos indefinidamente. El programa termina
cuando se introduce un número negativo. Finalmente el programa muestras la suma de
todos los números introducidos
"""
num=int(input("Digite un numero positivo: "))
print("Digitaste el numero: " + str(num))

suma=0

while num>0:
	suma = suma+num
	num=int(input("Digite otro numero positivo: "))
	print("Digitaste el numero: " + str(num))

print("Digitaste un numero negativo: " + str(num) + " Se termina el programa")
print("La suma fue: " + str(suma))