import xml.etree.ElementTree as ET

arbol = ET.parse("paises.xml")
root = arbol.getroot()

# El elemento raíz alamcena sus hijos en diccionarios y lo que se está realizando a continuación
# es recorriendo el diccionario
for child in root:
    # imprime la etiquetas de los hijos del elemento padre, así como el atrubuto que contienen
    print(child.tag, child.attrib)

