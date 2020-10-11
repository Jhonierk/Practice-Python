#Multiplicacion al reves

number=int(input("Digite un numero: "))

count = 10
while count>=1:
	multi = number * count
	print(number, "x", count, "=", multi)
	count = count-1