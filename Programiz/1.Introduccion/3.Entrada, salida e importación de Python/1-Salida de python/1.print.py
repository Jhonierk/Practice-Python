# Usamos la print()función para enviar datos al dispositivo de salida estándar (pantalla)
# También podemos enviar datos a un archivo , pero esto se discutirá más adelante.

#A continuación se da un ejemplo de su uso.

print('This sentence is output to the screen')

#A continuación se da otro ejemplo:

a = 5
print('The value of a is', a)

#En la segunda print()declaración, podemos notar que se agregó espacio entre la cadena y el valor de la variable 'a'.
# Esto es por defecto, pero podemos cambiarlo.

#La sintaxis real de la print()función es:

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

#Aquí objectsestán los valores que se van a imprimir.

#El sepseparador se usa entre los valores. Por defecto es un carácter de espacio.

#Una vez impresos todos los valores, endse imprime. Se establece por defecto en una nueva línea.

#El file es el objeto donde se imprimen los valores y su valor predeterminado es sys.stdout(pantalla).
#Aquí hay un ejemplo para ilustrar esto.

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')