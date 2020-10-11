#Cuando nuestro programa crezca, es una buena idea dividirlo en diferentes módulos.
#Un módulo es un archivo que contiene definiciones y declaraciones de Python.
#Los módulos de Python tienen un nombre de archivo y terminan con la extensión .py.
#Las definiciones dentro de un módulo se pueden importar a otro módulo o al intérprete interactivo en Python.
#Usamos la import palabra clave para hacer esto.

#Por ejemplo, podemos importar el mathmódulo escribiendo la siguiente línea:

import math

#Podemos utilizar el módulo de las siguientes formas:
#import math
print(math.pi)

#Ahora todas las definiciones dentro del mathmódulo están disponibles en nuestro alcance. 
#También podemos importar solo algunos atributos y funciones específicos, utilizando la from palabra clave. Por ejemplo:
from math import pi

#Al importar un módulo, Python busca en varios lugares definidos en sys.path. Es una lista de ubicaciones de directorio.
import sys
print(sys.path)

#https://www.programiz.com/python-programming/namespace