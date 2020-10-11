contador=0
miMail=input("Introduze tu correo: ")

for i in miMail:

	if (i=="@" or i=="."):
		contador=contador+1

if contador>=2:
	print("El correo es correcto")
else:
	print("El correo es incorrecto")