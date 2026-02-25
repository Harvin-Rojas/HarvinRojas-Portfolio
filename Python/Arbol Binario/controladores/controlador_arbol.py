# controladores/controlador_arbol.py

from modelos.arbol_bst import ArbolBinarioBusqueda

class ControladorArbol:

    def __init__(self):
        self.modelo = ArbolBinarioBusqueda()

    def agregar(self, valor):
        self.modelo.registrar(valor)

    def buscar(self, valor):
        return self.modelo.buscar(valor)

    def limpiar(self):
        self.modelo.limpiar()

    def obtener_recorridos(self):
        return self.modelo.reporte()

    @property
    def raiz(self):
        return self.modelo.raiz
