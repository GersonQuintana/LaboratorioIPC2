# Abrir un fichero en XML y presentarlo en pantalla

from xml.dom.minidom import parse
import xml.dom.minidom

# Abre el documento XML usando el analizador (parser) minidom
# modelo = xml.dom.minidom.parse("cd_catalogo.xml") #-> Modelo # #  del Documento en forma de árbol. Apertura por nombre
# O bien
fichero = open("cd_catalogo.xml")
modelo = parse(fichero) # Otra forma de abrir el fichero. Analiza el archivo y lo convierte en un árbol DOM

coleccion = modelo.documentElement # -> Almacena en 'coleccion' el elemento principal (raíz) del documeto XML (en este caso CATALOGO)
print ("El nombre de la coleccion es: %s \n" % coleccion.localName) #Obtiene el nombre del elemento raíz

print (coleccion.toxml()) # Devuelve todos los objetos hijos contenidos en el objeto raíz

