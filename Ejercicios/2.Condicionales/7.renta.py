"""
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 200000€ y 35000€	20%
Entre 350000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""

income = float(input("¿Cuál es tu renta anual? "))
if income < 10000:
    tax = 5
elif income < 20000:
    tax = 15
elif income < 35000:
    tax = 20
elif income < 60000:
    tax = 30
else:
    tax = 45
print("Tu tipo impositivo es " + str(tax) + "%")