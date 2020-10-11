#En Conversión de tipo explícito, los usuarios convierten el tipo de datos de un objeto en el tipo de datos requerido.
#Utilizamos las funciones predefinidas como int(), float(), str(), etc para llevar a cabo la conversión de tipos explícita.

#Este tipo de conversión también se denomina encasillado porque el usuario lanza (cambia) el tipo de datos de los objetos.

#Sintaxis: <required_datatype> (expresión)
#La conversión de tipos se puede realizar asignando la función de tipo de datos requerida a la expresión.

#Añadimos num_str y num_int variable.
num_int = 123
num_str = "456"


print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

#Nosotros convertimos num_strde tipo cadena (superior) a entero (inferior) usando la int()función para realizar la suma.
num_str = int(num_str)
print("Data type of num_str after Type Casting:",type(num_str))

#Después de convertir num_str a un valor entero, Python puede agregar estas dos variables.
num_sum = num_int + num_str

#Tenemos el num_sum valor y tipo de datos para ser un número entero.
print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))
