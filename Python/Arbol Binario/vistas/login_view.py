# vistas/login_view.py

import tkinter as tk
from tkinter import messagebox
from vistas.arbol_view import ArbolView

class LoginView:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("fase4_HarvinRojas")
        self.root.geometry("350x200")

        tk.Label(self.root, text="Aplicación: Arboles Binarios", font=("Arial", 14)).pack(pady=15)
        tk.Label(self.root, text="Estudiante: Harvin Rojas:").pack()
        tk.Label(self.root, text="Fecha:24/11/2025").pack()
        tk.Label(self.root, text="Contraseña:").pack()

        self.campo = tk.Entry(self.root, show="*")
        self.campo.pack(pady=5)

        tk.Button(self.root, text="Ingresar", command=self.validar).pack(pady=15)

        self.root.mainloop()

    def validar(self):
        if self.campo.get().strip() == "UNAD":
            self.root.destroy()
            ArbolView()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
