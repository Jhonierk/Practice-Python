#Un literal de cadena es una secuencia de caracteres entre comillas. Podemos usar comillas simples, dobles o triples para una cadena. 
#Y un carácter literal es un carácter único rodeado de comillas simples o dobles.

strings = "This is Python"
char = "C"
#Esto es Python es una cadena literal y C es un carácter literal.
multiline_str = """This is a multiline string with more than one line code."""
#El valor entre comillas triples """asignado a lamultiline_str es un literal de cadena de varias líneas.
unicode = u"\u00dcnic\u00f6de"
#La cuerda u "\ u00dcnic \ u00f6de"es un literal Unicode que admite caracteres distintos del inglés.
# En este caso,\ u00dcrepresenta Üy\ u00f6representa ö.
raw_str = r"raw \n string"
#r "cadena \ n sin procesar" es un literal de cadena sin formato.

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)