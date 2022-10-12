from service.nodo import Nodo

class ArbolBinario():
    def __init__(self, data):
        self.raiz = Nodo(data=data)

    def __agregar_recursivo(self, nodo, dato):
        if dato != nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__agregar_recursivo(nodo.derecha, dato)

    # Funciones públicas

    def agregar(self, dato):
        self.__agregar_recursivo(self.raiz, dato)
