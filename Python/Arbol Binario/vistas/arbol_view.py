# vistas/arbol_view.py

import tkinter as tk
from tkinter import messagebox

from controladores.controlador_arbol import ControladorArbol
from vistas.graficador import GraficadorArbol


class ArbolView:

    def __init__(self):
        self.controlador = ControladorArbol()

        self.root = tk.Tk()
        self.root.title("Árbol Binario de Búsqueda")
        self.root.state("zoomed")

        self.crear_interfaz()
        self.root.mainloop()

    def crear_interfaz(self):

        # ------------------- Entrada -------------------
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Ingrese un número: ").grid(row=0, column=0)
        self.entrada = tk.Entry(frame)
        self.entrada.grid(row=0, column=1)

        tk.Button(frame, text="Agregar Nodo", command=self.agregar).grid(row=0, column=2, padx=13)
        tk.Button(frame, text="Buscar Nodo", command=self.buscar).grid(row=0, column=3, padx=13)
        tk.Button(frame, text="Limpiar", command=self.limpiar).grid(row=0, column=4, padx=13)
        tk.Button(frame, text="Salir", command=self.root.destroy).grid(row=0, column=5, padx=13)

        # ------------------- Panel Árbol -------------------
        self.panel_arbol = tk.Canvas(self.root, bg="white", width=1200, height=500)
        self.panel_arbol.pack(pady=10)
        self.graficador = GraficadorArbol(self.panel_arbol)

        # ------------------- Recorridos -------------------
        panel_frame = tk.Frame(self.root)
        panel_frame.pack(pady=10)


        tk.Label(panel_frame, text="Preorden").grid(row=0, column=0)
        self.panel_pre = tk.Canvas(panel_frame, bg="#ffffff", width=250, height=50)
        self.panel_pre.grid(row=0, column=1, padx=10)

        tk.Label(panel_frame, text="Inorden").grid(row=0, column=2)
        self.panel_in = tk.Canvas(panel_frame, bg="#ffffff", width=250, height=50)
        self.panel_in.grid(row=0, column=3, padx=10)

        tk.Label(panel_frame, text="Posorden").grid(row=0, column=4)
        self.panel_pos = tk.Canvas(panel_frame, bg="#ffffff", width=250, height=50)
        self.panel_pos.grid(row=0, column=5, padx=10)
        

    # ---------------------------------------------------------
    # Métodos de la vista
    # ---------------------------------------------------------
    def agregar(self):
        try:
            valor = int(self.entrada.get())
            self.controlador.agregar(valor)
            self.entrada.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número entero")
            return
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return

        self.actualizar()

    def buscar(self):
        try:
            valor = int(self.entrada.get())
        except:
            messagebox.showerror("Error", "Ingrese un número entero")
            return

        if self.controlador.buscar(valor):
            messagebox.showinfo("Resultado", f"El nodo {valor} SÍ existe")
        else:
            messagebox.showwarning("Resultado", f"El nodo {valor} NO existe")

    def limpiar(self):
        self.controlador.limpiar()
        self.actualizar(paneles=True)

    def actualizar(self, paneles=False):
        # Dibujar Árbol
        self.graficador.dibujar_arbol(self.controlador.raiz)

        # Recorridos
        recorridos = self.controlador.obtener_recorridos()
        self.graficador.dibujar_recorrido(self.panel_pre, recorridos["preorden"])
        self.graficador.dibujar_recorrido(self.panel_in, recorridos["inorden"])
        self.graficador.dibujar_recorrido(self.panel_pos, recorridos["posorden"])
