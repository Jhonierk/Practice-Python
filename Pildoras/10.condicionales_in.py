print("Asignaturas disponibles: ")
print("Asignaturas optimas: Informatica basica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignaruta: ")

asignaruta=opcion.lower()

if asignaruta in ("informatica basica", "pruebas de software", "usabilidad y accesibilidad"):

	print("Asinatura escogida: " + asignaruta)

else:
	pritn("La asignaruta escogida no esta en la lista...")

#Para prueba de errores ya que python es case sensitive (no distingue de mayuscusas y minusculas)
#lower()minusculas,  upper()mayusculas.