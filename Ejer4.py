from grafo import Grafo
# Un empresa de telefonía celular dispone de la información de sus antenas, de las cuales se
# conoce: su ubicación (latitud y longitud), código de identificación, velocidad de transferencia
# en megabytes/segundos, y además las antenas a las que transmite y las distancias a cada una de
# estas. Implementar un algoritmo que permita resolver los siguientes requerimientos:
# a. utilizar un grafo no dirigido;
# b. cargar la información de antenas y la relación con las demás;
# c. determinar el tamaño del grafo;
# d. determinar el camino más corto para transmitir desde la antena ubicada en la capital de
# Mendoza a la antena ubicada en la capital de Misiones, utilizando el algoritmo de Dijkstra;
# e. encontrar el árbol de expansión mínimo del grafo, utilizando Prim o Kruskal;
# f. determinar si la antena con código “TGK-783” existe, de ser así mostrar toda su información.

grafo = Grafo(dirigido=False)

def ingresarAntenas(grafo):
    grafo.insertar_vertice("antena mendoza", data={"longitud":23, "latitud":12,"codigo":"ASC-456","velocidad":400})
    grafo.insertar_vertice("antena ER", data={"longitud":3, "latitud":12,"codigo":"AZB-416","velocidad":400})
    grafo.insertar_vertice("antena BSAS", data={"longitud":23, "latitud":12,"codigo":"AS1C-456","velocidad":400})
    grafo.insertar_vertice("antena Formosa", data={"longitud":23, "latitud":12,"codigo":"ASC-456","velocidad":400})
    grafo.insertar_vertice("antena Misiones", data={"longitud":23, "latitud":12,"codigo":"ASC-456","velocidad":400})
    grafo.insertar_vertice("antena Neuquen", data={"longitud":23, "latitud":12,"codigo":"TGK-783","velocidad":400})

grafo.insertar_arista(34,"antena mendoza","antena Formosa")
grafo.insertar_arista(32,"antena mendoza","antena ER")
grafo.insertar_arista(76,"antena mendoza","antena Neuquen")
grafo.insertar_arista(3,"antena mendoza","antena BSAS")
grafo.insertar_arista(9,"antena mendoza","antena Misiones")

grafo.insertar_arista(34,"antena ER","antena Neuquen")