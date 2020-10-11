"""
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
Si el divisor es cero el programa debe mostrar un error.
"""

num1=float(input("Digite un numero: "))
num2=float(input("Digite otro numero "))

div=num1/num2

if num2 == 0 or num1 == 0:
	print("Error no es posible dividir por 0")
else:
	print("La division es: "+ str(div))

"""
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)
"""