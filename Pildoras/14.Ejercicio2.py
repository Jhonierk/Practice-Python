"""
• Crea un programa que pida por teclado introducir una contraseña. La contraseña no
podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
errónea”
"""

print("bienvenido...")

contra=input("Por favor digite su contraseña: ")

cont=0

for i in range(len(contra)):

	if contra[i] ==" ":

		cont=1

if len(contra) <8 or cont>0:
	print("contraseña erronea")
else:
	print("Contraseña OK")
