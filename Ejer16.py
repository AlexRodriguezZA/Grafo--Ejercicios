from grafo import Grafo
# Implementar un grafo no dirigido para almacenar puntos turísticos de interés de un determi-
# nado país teniendo en cuenta los siguientes requerimientos:

# a. debe ser un grafo completo es decir que todos los vértices se deben conectar con todos;
# b. cargar los siguientes lugares (con sus coordenadas de latitud y longitud) templos de: Ate-
# nas (Partenón), Zeus (Olimpia), Hera (Olimpia), Apolo (Delfos),Poseidón (Sunión), Arte-
# misa (Éfeso) y Teatro de Dionisio (Acrópolis)
# c. hallar el árbol de expansión mínimo partiendo de cualquiera de estos lugares;
# d. hallar el camino más corto para ir desde el templo de Atenea, el Partenón, en Atenas hasta
# el templo de Apolo, en Delfos.

GrafoPunto = Grafo(dirigido=False)

def cargarGrafoTemplos(grafo):
    grafo.insertar_vertice("Atenas", data={"longitud":23, "latitud":12})
    grafo.insertar_vertice("Zeus", data={"longitud":45, "latitud":2})
    grafo.insertar_vertice("Hera", data={"longitud":2, "latitud":45})
    grafo.insertar_vertice("Apolo", data={"longitud":99, "latitud":56})
    grafo.insertar_vertice("Poseidón", data={"longitud":55, "latitud":23})
    grafo.insertar_vertice("Artemisa", data={"longitud":45, "latitud":19})
    grafo.insertar_vertice("Teatro de Dionisio", data={"longitud":32, "latitud":21})


def cargarGrafoAristas(grafo):
    #ATENAS
    grafo.insertar_arista(23, "Atenas", "Zeus")
    grafo.insertar_arista(4, "Atenas", "Hera")
    grafo.insertar_arista(53, "Atenas", "Apolo")
    grafo.insertar_arista(1, "Atenas", "Poseidón")
    grafo.insertar_arista(9, "Atenas", "Artemisa")
    grafo.insertar_arista(20, "Atenas", "Teatro de Dionisio")

    #ZEUS
    grafo.insertar_arista(13, "Zeus", "Hera")
    grafo.insertar_arista(12, "Zeus", "Apolo")
    grafo.insertar_arista(45, "Zeus", "Poseidón")
    grafo.insertar_arista(6, "Zeus", "Artemisa")
    grafo.insertar_arista(23, "Zeus", "Teatro de Dionisio")

    #HERA
    grafo.insertar_arista(3, "Hera", "Apolo")
    grafo.insertar_arista(43, "Hera", "Poseidón")
    grafo.insertar_arista(64, "Hera", "Artemisa")
    grafo.insertar_arista(52, "Hera", "Teatro de Dionisio")

    #APOLO
    grafo.insertar_arista(22, "Apolo", "Poseidón")
    grafo.insertar_arista(62, "Apolo", "Artemisa")
    grafo.insertar_arista(97, "Apolo", "Teatro de Dionisio")

    #POSEIDON
    grafo.insertar_arista(5, "Poseidón", "Artemisa")
    grafo.insertar_arista(2, "Poseidón", "Teatro de Dionisio")

    #ARTEMISA
    grafo.insertar_arista(24, "Artemisa", "Teatro de Dionisio")

def buscarCaminoMascorto(grafo, verticeOrigen, verticeDestino):
    dios1 = grafo.buscar_vertice(verticeOrigen)
    dios2 = grafo.buscar_vertice(verticeDestino)

    caminocorto = grafo.dijkstra(dios1, dios2)

    costo = None
    while(not caminocorto.pila_vacia()):
        dato = caminocorto.desapilar()
        if(dato[1][0] == verticeDestino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            verticeDestino = dato[1][1]
    print('el costo total del camino es:', costo, " KM")

def expansionMinima(grafo):
    arbolExpancionMinima = []
    arbolExpancionMinima = grafo.prim();

    print("Arbol de expansion minima")
    for e in arbolExpancionMinima:
        print(e)

#PUNTO B
cargarGrafoTemplos(GrafoPunto)
cargarGrafoAristas(GrafoPunto)

#PUNTO C
expansionMinima(GrafoPunto)

#PUNTO D
print()
buscarCaminoMascorto(GrafoPunto,"Atenas","Apolo")











