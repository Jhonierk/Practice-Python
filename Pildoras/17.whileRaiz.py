import math

print("Raiz cuadrada...")
num=int(input("Digite numero: "))

intentos=0

while num<0:
	pritn("No se haya la raiz de negativo")

	if intentos == 2:
		print("Demasiado intentos...")
		break;

	num=int(input("Digite numero: "))
	if num<0:
		intentos=intentos+1

if intentos<2:
	solucion=math.sqrt(num)
	print("La raiz cuadrada de: " + str(num) + " es " + str(solucion))