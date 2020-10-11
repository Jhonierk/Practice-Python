for name in "python":

	if name == "h":
		#La funcion continue hace continuar la siguientes iteraciones, ignora la "h"
		continue

	print("Imprime cada lentra: " + name)


#Con esto se cuenta la cantidad de letras ignorando el espacio
nombre = "Leidy Te amo"

count=0

for i in nombre:

	if i == " ":
		continue
	count+=1

print(count)