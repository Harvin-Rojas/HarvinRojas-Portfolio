# modelos/arbol_bst.py

from modelos.estructura_base import EstructuraBase
from modelos.nodo import Nodo


class ArbolBinarioBusqueda(EstructuraBase):

    def __init__(self):
        self.raiz = None

    # ---------------------------------------------------------
    # Registrar → insertar nodo
    # ---------------------------------------------------------
    def registrar(self, valor):
        if not isinstance(valor, int):
            raise ValueError("El valor debe ser un entero")

        if self.raiz is None:
            self.raiz = Nodo(valor)
            return

        self._insertar(self.raiz, valor, nivel=1)

    def _insertar(self, nodo, valor, nivel):
        if nivel == 4:
            raise Exception("No se puede exceder 4 niveles.")

        if valor == nodo.valor:
            raise Exception("El nodo ya existe")

        if valor < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(valor)
            else:
                self._insertar(nodo.izq, valor, nivel + 1)
        else:
            if nodo.der is None:
                nodo.der = Nodo(valor)
            else:
                self._insertar(nodo.der, valor, nivel + 1)

    # ---------------------------------------------------------
    # Buscar nodo
    # ---------------------------------------------------------
    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        if valor < nodo.valor:
            return self._buscar(nodo.izq, valor)
        return self._buscar(nodo.der, valor)

    # ---------------------------------------------------------
    # Eliminar (no se usa pero es obligatorio en la abstracción)
    # ---------------------------------------------------------
    def eliminar(self, valor=None):
        pass  # no requerido en esta práctica

    # ---------------------------------------------------------
    # Recorridos
    # ---------------------------------------------------------
    def preorden(self):
        res = []
        self._pre(self.raiz, res)
        return res

    def _pre(self, nodo, res):
        if nodo:
            res.append(nodo.valor)
            self._pre(nodo.izq, res)
            self._pre(nodo.der, res)

    def inorden(self):
        res = []
        self._in(self.raiz, res)
        return res

    def _in(self, nodo, res):
        if nodo:
            self._in(nodo.izq, res)
            res.append(nodo.valor)
            self._in(nodo.der, res)

    def posorden(self):
        res = []
        self._pos(self.raiz, res)
        return res

    def _pos(self, nodo, res):
        if nodo:
            self._pos(nodo.izq, res)
            self._pos(nodo.der, res)
            res.append(nodo.valor)

    # ---------------------------------------------------------
    # Reporte genérico solicitado por abstracción
    # ---------------------------------------------------------
    def reporte(self):
        return {
            "preorden": self.preorden(),
            "inorden": self.inorden(),
            "posorden": self.posorden()
        }

    # ---------------------------------------------------------
    # Limpiar árbol
    # ---------------------------------------------------------
    def limpiar(self):
        self.raiz = None
