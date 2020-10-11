#En la conversión de tipos implícitos, Python convierte automáticamente un tipo de datos en otro tipo de datos.
# Este proceso no necesita la participación del usuario.

#Veamos un ejemplo en el que Python promueve la conversión del tipo de datos más bajo (entero)
#al tipo de datos más alto (flotante) para evitar la pérdida de datos

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo
#Agregamos dos variables num_int y num_flo, almacenando el valor en num_new.

#Veremos el tipo de datos de los tres objetos respectivamente.
print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))
#En la salida, podemos ver el tipo de datos de num_intes un integertiempo el tipo de datos denum_floes un float.

#Además, podemos ver el num_newtiene un floattipo de datos porque Python siempre convierte 
#tipos de datos más pequeños en tipos de datos más grandes para evitar la pérdida de datos.
print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))