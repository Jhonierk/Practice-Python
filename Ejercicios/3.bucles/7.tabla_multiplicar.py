"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""
num=int(input("Digite el numero para ver su tabla: "))

for i in range(1, 11):
	multiplicar=i*num
	print(str(i) + " x " + str(num) + " = " + str(multiplicar))

"""
otra forma:
"""

print("Otra tabla: ")

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
