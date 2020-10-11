for i in range(10,51,5):
	print(f"Leidy te amo {i}")

for i in range(10,0,-2):
	print(i)

#-------------------------------------
valido=False

email=input("Digite su correo: ")

for i in range(len(email)):

	if (email[i]=="@" or email[i]=="."):

		valido=True

if valido:

	print("Correo correcto")

else:
	print("Correo incorrecto")