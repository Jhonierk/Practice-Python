#A veces nos gustaría formatear nuestra salida para que se vea atractiva.
#Esto se puede hacer usando el str.format()método. Este método es visible para cualquier objeto de cadena.
x=5; y=10
print("El valor de x es: {} & y es: {}".format(x,y))

#Aquí, las llaves {} se utilizan como marcadores de posición.
#Podemos especificar el orden en el que se imprimen utilizando números (índice de tupla).
print('I love {0} and {1}'.format('Leidy','Kira'))
print('I love {1} and {0}'.format('Leidy','Kira'))

#Incluso podemos usar argumentos de palabras clave para formatear la cadena.
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'Jhonnyer'))

#También podemos dar formato a cadenas como el viejo sprintf()
#estilo usado en el lenguaje de programación C . Usamos el % operador para lograr esto.
x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)