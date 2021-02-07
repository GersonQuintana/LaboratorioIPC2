# Obtener el nombre del objeto raíz

import xml.etree.ElementTree as ET

# El método 'parse' lee todo el archivo, analiza la estructura contenida en XML
# y la reproduce en una representación accedible para Python, es decir,
# crear la estructura de árbol, al cual hay que referirse para extraer información
# contenida dentro del archivo XML.
arbol = ET.parse("libros.xml")

#Obtiene el elemento raíz
root = arbol.getroot()

# Obtiene la etiqueta del elemento raíz
nombre = root.tag
print(nombre)

