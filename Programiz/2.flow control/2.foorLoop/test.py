#programa que pide donde inicia y termina el conteo
num1=int(input("Digite un numero: "))
num2=int(input("Digite un numero mayor al anterior: "))


if num1 < num2:
	print("numero de inicio: " + str(num1))
	print("numero final: " + str(num2))

	for i in range(num1, num2):
		print(i)
	

else:
	print("Digitaste mal un numero")

