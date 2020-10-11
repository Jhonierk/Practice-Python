"""
Create a program to check wheteher a number is positibe or negative or 0. For this, create a variable
named number & assig a float value to it based on the user input.
then using a if stateent, check if the number variable is positive or negative or 0.
*if number is positive, print "The numbes is positive"
*if nuber is negative, print "The number is negative
*(and) if number is 0, print "The number is 0"

Cree un programa para comprobar si un numero es positivo o negativo o 0. Para ello, cree una variable llamada
numero y asignarle un valor flotante basado en la entrada del usuario.
luego, usando una declaración if, verifique si la variable numérica es positiva o negativa o 0.
* si el número es positivo, escriba "Los números son positivos"
* si nuber es negativo, escriba "El número es negativo
* (y) si el número es 0, imprima "El número es 0"
"""

number = float(input("Digite un numero: "))

if number > 0:
	print("El numero es positivo: " + str(number))
elif number < 0:
	print("El numero es negativo: " + str(number))
elif number == 0:
	print("El numero es zero: " + str(number))
else:
	print("Haz ingresado mal")