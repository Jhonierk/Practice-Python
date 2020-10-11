def greet(mascota):
	print("Tu mascota es: ", mascota)
	print("Leidy te amo")

greet("kira")


num1 =int(input("Digite el primer numero: "))
num2 =int(input("Digite el segundo numero: "))
print("Seleccione la opcion: \n 1.suma \n 2.resta \n 3.multi \n 4.Divi")
select=int(input("---> :"))


def suma (num1, num2):
	result= num1+num2
	print("EL resultado es: " + str(result))

def resta (num1, num2):
	result= num-num2
	print("EL resultado es: " + str(result))

def multi (num1, num2):
	result= num1*num2
	print("EL resultado es: " + str(result))

def divi (num1, num2):
	result= num1/num2
	print("EL resultado es: " + str(result))

if select == 1:
	suma(num1, num2)
elif select == 2:
	resta (num1, num2)
elif select == 3:
	multi (num1, num2)
elif select == 4:
	divi (num1, num2)
