# modelos/estructura_base.py

from abc import ABC, abstractmethod

class EstructuraBase(ABC):

    @abstractmethod
    def registrar(self, valor):
        pass

    @abstractmethod
    def eliminar(self, valor=None):
        pass

    @abstractmethod
    def reporte(self):
        pass

    def limpiar(self):
        pass
