"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

contra = ("ljk180518")
password=""

while password.lower() != contra:
	password = input("introduzca la contraseña :")

print("Contraseña correcta...")
