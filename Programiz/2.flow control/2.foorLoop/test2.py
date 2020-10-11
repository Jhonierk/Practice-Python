#Tabla de multiplicar


num=int(input("Digite que numero multiplicar: "))

for i in range (11):
	multi=i*num
	print(str(i) + "x" + str(num) + "=" + str(multi))