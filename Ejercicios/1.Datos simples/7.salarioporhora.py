"""
Escribir un programa que pregunte al usuario por el número
de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
"""
horas=int(input("Ingrese horas trabajadas: "))
coste=int(input("Su pago por hora es?: "))

calcu= round(horas*coste)

print("Puedes cobrar: " + str(calcu))