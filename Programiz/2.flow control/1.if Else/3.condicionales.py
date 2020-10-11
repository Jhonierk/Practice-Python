score = int(input("Digite su nota: "))

if score >10 or score <0:
	print("Has ingresado un numero mal: " + str(score))
elif score >= 8:
	print("Has pasado el examen con: " +str(score))
else:
	print("Lo sentimos has reprobado con: " + str(score))
	