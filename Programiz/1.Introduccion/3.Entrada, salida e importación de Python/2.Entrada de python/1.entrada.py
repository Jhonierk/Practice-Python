#Hasta ahora, nuestros programas eran estáticos. El valor de las variables se definió o codificó en el código fuente.
#Para permitir la flexibilidad, es posible que deseemos tomar la entrada del usuario. En Python, tenemos la input()
#función para permitir esto. La sintaxis de input() es:
#input([prompt])

#donde prompt está la cadena que deseamos mostrar en la pantalla. Es opcional.

num1=int(input("Digite numero 1: "))
num2=int(input("Digite numero 2: "))

sumar=(num1+num2)
print(sumar)

#Aquí, podemos ver que el valor ingresado 10es una cadena, no un número.
#Para convertir esto en un número podemos usar las funciones int()o float().
int('10')
float('10')

#Esta misma operación se puede realizar utilizando la eval() función.
#Pero lo eval lleva más allá. Puede evaluar expresiones pares, siempre que la entrada sea una cadena
a='13+12'
suma=(eval(a))
print(suma)
 