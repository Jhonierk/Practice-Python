"""
Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
correcta si solo tiene una “@” y si tiene uno o más “.”
"""

email=input("Ingrese correo: ")

cont1=0
cont2=0

for i in range(len(email)):

	if email[i]=="@":

		cont1=cont1+1

	if email[i]==".":

		cont2=cont2+1

if cont1>1 or cont2 == 0:

	print("email incorrecto")

else:

	print("Email Correcto")