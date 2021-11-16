from grafo import Grafo
# Implementar un grafo no dirigido que permita cargar puertos y las aristas que conecten dichos
# puertos, que permita resolver las siguientes tareas:
# a. cada arista debe tener la distancia que separa dichos puertos;
# b. realizar un barrido en profundidad desde el primer puerto en el grafo;
# c. determinar el camino más corto desde puerto Madero al puerto de Rodas;
# d. determinar el puerto con mayor número de aristas y eliminarlo.

grafo = Grafo(dirigido=False)

def insertarVertice(grafo):
    grafo.insertar_vertice("Puerto madero")
    grafo.insertar_vertice("Puerto de Buenos Aires")
    grafo.insertar_vertice("Muelle YPF")
    grafo.insertar_vertice("Rodas")
    grafo.insertar_vertice("La Plata")
    grafo.insertar_vertice("Muelle EAPVC")

def insertarAristas(grafo):
    grafo.insertar_arista(4,"Puerto madero","La Plata")
    grafo.insertar_arista(60,"Puerto madero","Puerto de Buenos Aires")
    grafo.insertar_arista(12,"Puerto madero","Muelle YPF")
    grafo.insertar_arista(31,"Puerto madero","Rodas")
    grafo.insertar_arista(5,"Puerto madero","Muelle EAPVC")

    grafo.insertar_arista(15,"La Plata","Puerto de Buenos Aires")
    grafo.insertar_arista(34,"La Plata","Muelle YPF")
    grafo.insertar_arista(20,"La Plata","Rodas")

    grafo.insertar_arista(15,"Muelle EAPVC","Rodas")

    grafo.insertar_arista(43,"Muelle YPF","Muelle EAPVC")

def caminoMasCorto(grafo,verticeOrigen,verticeDestino):
    puerto1 = grafo.buscar_vertice(verticeOrigen)
    puerto2 = grafo.buscar_vertice(verticeDestino)

    caminocorto = grafo.dijkstra(puerto1,puerto2)

    costo = None
    while(not caminocorto.pila_vacia()):
        dato = caminocorto.desapilar()
        if(dato[1][0] == verticeDestino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            verticeDestino = dato[1][1]
    print('el costo total del camino es:', costo, " KM")

def puertoConMasAristas(grafo):
    Puertos = ["Puerto madero","Puerto de Buenos Aires","Muelle YPF","Rodas","La Plata","Muelle EAPVC"]
    for puerto in Puertos:
        posPuerto = grafo.buscar_vertice(puerto)
        ListaAristas = grafo.inicio.obtener_elemento(posPuerto)
        print(f"Puerto {puerto}")
        print(ListaAristas["aristas"].tamanio())



    




        

    

insertarVertice(grafo)
insertarAristas(grafo)

grafo.barrido_profundidad(1)
print()
caminoMasCorto(grafo,"Puerto madero","Rodas")

puertoConMasAristas(grafo)

