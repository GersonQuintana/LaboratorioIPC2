# Extraer un fichero y modificarlo

import xml.dom.minidom

# El método 'parse' lee todo el archivo, analiza la estructura contenida en XML
# y la reproduce en una representación accedible para Python, es decir,
# crear la estructura de árbol, al cual hay que referirse para extraer información
# contenida dentro del archivo XML.
arbolDom = xml.dom.minidom.parse("cd_catalogo.xml")

# Obtiene el elemento principal del documento XML, es decir, aquel
# que contiene a todos los demás elementos
objetoPrincipal = arbolDom.documentElement 

# Imprime el nombre del objeto principal
print("El nombre del objeto raíz es ", objetoPrincipal.localName)

# Obtiene todos los elementos con el nombre de etiqueta "CD" que son hijos
# del objetoPrincipal
listaEtiquetas = objetoPrincipal.getElementsByTagName("CD")

for hijoCD in listaEtiquetas:
    print("*****CD*****")
    titulo = hijoCD.getElementsByTagName("TITULO")[0]
    print("Título: ", titulo.childNodes[0].data) # En este caso es la posición 0, ya que obtiene todos los nodos hijos, incluyendo el nodo 
                                     # el nodo desde el que se invocó y obtiene su contenido
    
    # Se coloca [0] ya que estamos accediendo a un elemento de una lista
    artista = hijoCD.getElementsByTagName("ARTISTA")[0]
    print("Artista: ", artista.childNodes[0].data)

    pais = hijoCD.getElementsByTagName("PAIS")[0]
    print("País: ", pais.childNodes[0].data)

    precio = hijoCD.getElementsByTagName("PRECIO")[0]
    print("Precio: ", precio.childNodes[0].data)

    anno = hijoCD.getElementsByTagName("ANNO")[0]
    print("Año: ", anno.childNodes[0].data)

    print()