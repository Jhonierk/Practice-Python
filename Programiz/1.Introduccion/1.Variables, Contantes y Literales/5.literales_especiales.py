#Python contiene un literal especial, es decir None. Lo usamos para especificar que el campo no ha sido creado.

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

#definimos una menu función. En el interior menu, cuando establecemos el argumento como drink entonces, se muestra Available.
# Y, cuando el argumento es food, se muestra None.

menu(drink)
menu(food)