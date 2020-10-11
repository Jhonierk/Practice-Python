edad=int(input("Digite su edad: "))

while edad <5 or edad>100:
	print("Has digitado edad incorrecta. Vuelve a intentarlo!")
	edad=int(input("Digite su edad: "))

print("Has digitado correctamente")
print("Edad digitada : "+ str(edad))