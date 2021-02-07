from xml.dom import minidom

Ordenador1 = ['Pentium M', '512MB']
Ordenador2 = ['Pentium Core 2', '1024MB']
Ordenador3 = ['Pentium Core Duo', '1024MB']
listaOrdenadores = [Ordenador1, Ordenador2, Ordenador3]

# Abro un modelo DOM en modo implementar
DOMimpl = minidom.getDOMImplementation() 

# Crear el documento con la etiqueta principal estacionesTrabajo (etiqueta raiz)
# No se crear el ducumento como tal, sino que solo almacena en "xmldoc" la información que va a tener el documento
xmldoc = DOMimpl.createDocument(None,"estacionesTrabajo", None)
doc_root = xmldoc.documentElement # Almacena en 'doc_root' el nombre del elemento principal del documento

# Recorro la lista de ordenadores
for ordenador in listaOrdenadores:
    
    #Crear Nodo...
    nodo = xmldoc.createElement("Ordenador") # Crea una etiqueta 'Ordenador', la cual se pasa como parámetro

    # Crear un subnodo, llamado procesador
    elemento = xmldoc.createElement('Procesador')

    # Le añado un nodo de texto, y le asigno la posición 0 de la lista
    elemento.appendChild(xmldoc.createTextNode(ordenador[0])) # Entre la etiqueta 'Procesador' va a escribir
                                                              # lo que tenga la lista ordenador en la posición 0
                                                              # y lo va a almacenar en 'elemento'

    # Añado el subnodo al nodo anterior
    nodo.appendChild(elemento) # La etiqueta procesador se va a agregar a un objeto superior llamado 'ordenador'
    
    # Idéntico.
    elemento = xmldoc.createElement('Memoria')
    elemento.appendChild(xmldoc.createTextNode(ordenador[1]))
    nodo.appendChild(elemento)

    # (*)... que se añade como hijo al doc_root
    doc_root.appendChild(nodo) # Ahora el objeto 'nodo' (Ordenador) va a estar envuelto por la etiqueta 'estacionesTrabajo'

# Recorrer para presentar en pantalla la lista de los nodos
listaNodos = doc_root.childNodes # La propiedad de solo lectura Node.childNodes devuelve una 
                                 # colección de hijos nodes del elemento dado donde el primer nodo hijo es asignado un índice 0.
                                 # En este caso, todo los hijos del objeto 'estacionTrabajo'
for nodo in listaNodos:
    print (nodo.toprettyxml())

# Guardar la información en un fichero de texto
fichero = open("ordenadores.xml", 'w')
# fichero.write(xmldoc.toxml())
fichero.write(xmldoc.toprettyxml()) # --> diferentes formas de guardar un fichero xml
# fichero.write(xmldoc.toprettyxml(encoding="utf-8"))
fichero.close()