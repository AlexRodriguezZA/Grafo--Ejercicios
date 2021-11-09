from grafo import Grafo

# Partiendo del árbol genealógico de los dioses griegos que se observa en la imagen del ejercicio
# 20 de la guía de árboles (capítulo X), convertirlo en un grafo y resolver las siguientes actividades:
# a. además del nombre de los dioses, deberá cargar una breve descripción de quien es o lo que
# representa, no más de 20 palabras;
# b. deberá cargar todas las relaciones entre los distintos dioses: padre, madre, hijo, hermano,
# pareja, la etiquetas de dichas aristas son estos nombre de relación.
# c. dado el nombre de un dios mostrar los hijos de este;
# d. dado el nombre de un dios mostrar su nombre, padre, madre, hermanos y sus hijos;
# e. determinar si existe relación directa entre dos vértice cualquieras, de ser así cual es la rela-
# ción entre ambos;
# f. dados dos dioses determinar el camino más corto entre estos y mostrarlo. Considere como
# camino más corto el que tenga menor número de aristas;
# g. realizar un barrido en profundidad y amplitud de dicho grafo;
# h. realizar un barrido mostrando el nombre de cada dios y el de su madre;
# i. mostrar todos los ancestros de un determinado dios;
# j. mostrar todos los nietos de Cronos;
# k. mostrar todos los hijos de Tea;
# l. persista los datos del grafo en archivos, uno para los vértices y otro para las aristas.
GrafoDioses = Grafo(dirigido=False)

def cargarVertices(GrafoDioses):
    GrafoDioses.insertar_vertice('Urano')
    GrafoDioses.insertar_vertice('Themis')
    GrafoDioses.insertar_vertice('mnemosyne')
    GrafoDioses.insertar_vertice("Hyperion")
    GrafoDioses.insertar_vertice("Theia") 
    GrafoDioses.insertar_vertice("Krios") 
    GrafoDioses.insertar_vertice('Cronos')
    GrafoDioses.insertar_vertice('Rea')
    GrafoDioses.insertar_vertice("Kdios")
    GrafoDioses.insertar_vertice("Phombe")
    GrafoDioses.insertar_vertice("Iapetos") 
    GrafoDioses.insertar_vertice("Okeanos")
    GrafoDioses.insertar_vertice("Tethds")
    GrafoDioses.insertar_vertice("Selene")
    GrafoDioses.insertar_vertice("Eos")
    GrafoDioses.insertar_vertice("Helios")
    GrafoDioses.insertar_vertice("Prometheus")
    GrafoDioses.insertar_vertice("Epimetheus")
    GrafoDioses.insertar_vertice("Atlas")
    GrafoDioses.insertar_vertice("pleione")
    GrafoDioses.insertar_vertice('Zeus')
    GrafoDioses.insertar_vertice('Hades')
    GrafoDioses.insertar_vertice('Demeter')
    GrafoDioses.insertar_vertice('Poseidon')
    GrafoDioses.insertar_vertice('Hestia')
    GrafoDioses.insertar_vertice('Hera')
    GrafoDioses.insertar_vertice('Leto')
    GrafoDioses.insertar_vertice('Semele')
    GrafoDioses.insertar_vertice('Maia')
    GrafoDioses.insertar_vertice('Persefone')
    GrafoDioses.insertar_vertice('Aphrodite')
    GrafoDioses.insertar_vertice('Ares')
    GrafoDioses.insertar_vertice('Hephanistos')
    GrafoDioses.insertar_vertice('Athena')
    GrafoDioses.insertar_vertice('Apollo')
    GrafoDioses.insertar_vertice('Artemis')
    GrafoDioses.insertar_vertice('Dionysos')
    GrafoDioses.insertar_vertice('Penelopeia')
    GrafoDioses.insertar_vertice('Phobos')
    GrafoDioses.insertar_vertice('Deimos')
    GrafoDioses.insertar_vertice('Eros')
    GrafoDioses.insertar_vertice('Himerios')
    GrafoDioses.insertar_vertice('Hermaphrodite')
    GrafoDioses.insertar_vertice('Pan')
    GrafoDioses.insertar_vertice('Hermes')







def cargarAristas(GrafoDioses):
    GrafoDioses.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'mnemosyne', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Hyperion', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Krios', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Phombe', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Tethds', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Rea', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Urano', 'Kdios', data={'relacion': ['padre', 'hijo']})
   

    GrafoDioses.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Hera', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Hestia', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Poseidon', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['hermano']})

    GrafoDioses.insertar_arista(1, 'Rea', 'Zeus', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Rea', 'Hera', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Rea', 'Hestia', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Rea', 'Poseidon', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Rea', 'Hades', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Rea', 'Demeter', data={'relacion': ['madre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Kdios', 'Phombe', data={'relacion': ['hermano']})
    GrafoDioses.insertar_arista(1, 'Kdios', 'Phombe', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Kdios', 'Leto', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Phombe', 'Leto', data={'relacion': ['madre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})


    GrafoDioses.insertar_arista(1, 'Okeanos', 'pleione', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Tethds', 'pleione', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Okeanos', 'Tethds', data={'relacion': ["pareja"]})
    GrafoDioses.insertar_arista(1, 'Okeanos', 'Tethds', data={'relacion': ["hermano"]})

    GrafoDioses.insertar_arista(1, 'Atlas', 'pleione', data={'relacion': ["hermano"]})
    GrafoDioses.insertar_arista(1, 'Atlas', 'pleione', data={'relacion': ["pareja"]})
    GrafoDioses.insertar_arista(1, 'Atlas', 'Maia', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'pleione', 'Maia', data={'relacion': ['madre', 'hijo']})



    GrafoDioses.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Hera', data={'relacion': ['hermano']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Hestia', data={'relacion': ['hermano']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Poseidon', data={'relacion': ['hermano']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Demeter', data={'relacion': ['hermano']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Hera', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Leto', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Semele', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Maia', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Ares', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Hephanistos', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Semele', 'Dionysos', data={'relacion': ['madre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Phobos', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Deimos', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Eros', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Himerios', data={'relacion': ['madre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Hermes', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Aphrodite', 'Hermaphrodite', data={'relacion': ['madre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Hermes', 'Penelopeia', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Penelopeia', 'Pan', data={'relacion': ['madre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Hades', 'Persefone', data={'relacion': ['pareja']})


    GrafoDioses.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Zeus', 'Persefone', data={'relacion': ['padre', 'hijo']})

    GrafoDioses.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Apollo', 'Persefone', data={'relacion': ['hermano']})

    GrafoDioses.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Theia', 'Hyperion', data={'relacion': ['pareja']})
    GrafoDioses.insertar_arista(1, 'Theia', 'Hyperion', data={'relacion': ['hermano']})

    GrafoDioses.insertar_arista(1, 'Hyperion', 'Helios', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Hyperion', 'Eos', data={'relacion': ['padre', 'hijo']})
    GrafoDioses.insertar_arista(1, 'Hyperion', 'Selene', data={'relacion': ['padre', 'hijo']})



def MostrarHijosDios(GrafoDioses,nombreDios):
    posicionDios = GrafoDioses.buscar_vertice(nombreDios)
    dios = GrafoDioses.inicio.obtener_elemento(posicionDios);
    for i in range(dios["aristas"].tamanio()):
        relacion = dios["aristas"].obtener_elemento(i)
        if "hijo" in relacion['data']['relacion']:
            print(relacion["destino"])

def mostrarParientesDios(GrafoDioses, nombreDios):
    posicionDios = GrafoDioses.buscar_vertice(nombreDios)
    diosBuscado = GrafoDioses.inicio.obtener_elemento(posicionDios)
    for i in range(diosBuscado["aristas"].tamanio()):
        familiar = diosBuscado["aristas"].obtener_elemento(i)
        print(familiar["destino"])

def relaciondirecta(grafo,verticeInicio,verticeFinal):
    control = grafo.es_adyacente(verticeInicio,verticeFinal)
    if (control == True):
        print("Tiene relacion de: ")
        posicion = grafo.buscar_vertice(verticeInicio)
        diosPrincipal = grafo.inicio.obtener_elemento(posicion)
        for i in range(diosPrincipal["aristas"].tamanio()):
            diosPariente = diosPrincipal["aristas"].obtener_elemento(i)
            if (diosPariente["destino"]==verticeFinal):
                print(diosPariente['data']['relacion'])
    else:
        print("No tiene relacion")

def mostraAncestro(grafo,verticeOrigen):  #RECURSIVO
    pos = grafo.buscar_vertice(verticeOrigen)
    dios = grafo.inicio.obtener_elemento(pos)
    for i in range (dios["aristas"].tamanio()):
        nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
        ancestro = dios["aristas"].obtener_elemento(i)
        if (len(ancestro["data"]['relacion']) > 1):
            if(ancestro["data"]['relacion'][1] == 'padre' or ancestro["data"]['relacion'][1] == 'madre'):
                    print(nombre_dios, ancestro["data"]['relacion'])
                    mostraAncestro(grafo,nombre_dios)

def NietosCronos(grafo,diosIngresado):
    vectorHijos = [];
    pos = grafo.buscar_vertice(diosIngresado)
    hijosCronos = grafo.inicio.obtener_elemento(pos)
    for i in range(hijosCronos["aristas"].tamanio()):
        hijoCrono = hijosCronos["aristas"].obtener_elemento(i)
        nombreHijoCrono = hijosCronos['aristas'].obtener_elemento(i)['destino']
        if (len(hijoCrono["data"]["relacion"])==2):
            if (hijoCrono["data"]["relacion"][1] == "hijo"):
                vectorHijos.append(nombreHijoCrono)
                #OBTENEMOS LOS HIJOS DE CRONOS
    for hijo in vectorHijos:
        posHijoCrono = grafo.buscar_vertice(hijo)
        NietoCronos = grafo.inicio.obtener_elemento(posHijoCrono)
        for j in range(NietoCronos["aristas"].tamanio()):
            nieto = NietoCronos["aristas"].obtener_elemento(j)
            nombreNieto = NietoCronos['aristas'].obtener_elemento(j)['destino']
            if (len(nieto["data"]["relacion"])==2):
                if (nieto["data"]["relacion"][1] == "hijo"):
                        print("Nietos de crono: " ,nombreNieto)

def hijosTheia(grafo):
    pos = grafo.buscar_vertice("Theia")
    diosaTheia = grafo.inicio.obtener_elemento(pos)
    for i in range(diosaTheia["aristas"].tamanio()):
        hijosDeTheia = diosaTheia["aristas"].obtener_elemento(i)
        if (len(hijosDeTheia["data"]["relacion"]) == 2):
            if hijosDeTheia["data"]["relacion"][1] == "hijo":
                print(hijosDeTheia["destino"]) 

def caminoMasCorto(grafo,verticeOrigen,VerticeDestino):
    dios1 = grafo.buscar_vertice(verticeOrigen)
    dios2 = grafo.buscar_vertice(VerticeDestino)
    camino = grafo.dijkstra(dios1,dios2)
    costo = None
    while(not camino.pila_vacia()):
        dato = camino.desapilar()
        if(dato[1][0] == VerticeDestino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            VerticeDestino = dato[1][1]
    print('el costo total del camino es:', costo)

#PUNTO B
cargarVertices(GrafoDioses)
cargarAristas(GrafoDioses)

# #PUNTO C
# diosBuscado = input("Ingrese nombre de un dios")
# print(f"Los hijos de {diosBuscado} son: ")
# MostrarHijosDios(GrafoDioses,diosBuscado)

# #PUNTO D
# diosBuscado = input("Ingrese nombre de un dios")
# print(f"Los familiares de {diosBuscado} son: ")
# mostrarParientesDios(GrafoDioses,diosBuscado)

#PUNTO E
relaciondirecta(GrafoDioses,"Persefone","Demeter")

#PUNTO F
# caminoMasCorto(GrafoDioses,"Urano","Cronos")

#PUNTO G
# print("Barrido en profundidad")
# GrafoDioses.barrido_profundidad(0)
# print("Barrido en amplitud")
# GrafoDioses.barrido_amplitud(0)

#PUNTO H
#GrafoDioses.MadresDeDioses(0)

# #PUNTO I
# mostraAncestro(GrafoDioses,"Cronos")

#PUNTO J
# NietosCronos(GrafoDioses,"Cronos")

#PUNTO K
# print("Los hijos de theia son:")
# hijosTheia(GrafoDioses)
