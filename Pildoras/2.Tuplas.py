#Reglas:
#Las tuplas son listas inmutables, Es decir, no se pueden modificar despues de su creacion
#*No permiten añadir, eliminar, mover elementos (no append, extend, remove)
#Apartir de la vercsion 2.7+ se permite realizar busquedas con index
#Si permite comprobar si un elemento se encuentra en la tupla

#Ventajas de tuplas:
#Mas rapidas, Menos espacio, Formatean Strings, Pueden utilizarse  como claves en diccionarioss (listas no)

#Para convertir una lista en tupla se realiza lo siguiente:
milista=["Kira", 69,6,2014,69]
mitupla=tuple(milista)

#imprime el contenido de la tupla
print(milista)

#Comprobar si kira esta dentro de la tupla con "in"
print("Kira" in milista)#si imprime true significa que si esta en la tupla

#Con el metodo count nos dice cuantos elementos esta dentro de tupla
print(mitupla.count(69)) #en este caso el 69 se encuentra 2 veces asi que imprime 2

#El mentodo len nos permite averiguar la longitud de una tupla
print(len(mitupla)) #En este caso imprime 5 elementos 

#Tuplas unitarias:
mituplas=("Juan",)
print(len(mituplas))

#Empaquetado de tupla:
mituplaemp="Kira", 69, 6, 2014
print(mituplaemp)

#Desempaquetado de tupla:
mituplades=("Kira", 9, 1, 2014)
nombre, dia, mes, anio=mituplades #Asigna el valos de cada variable cada parametro de mituplades
print(nombre)
print(dia)
print(anio)
print(mes)

