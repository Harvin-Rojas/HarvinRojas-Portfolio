import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from abc import ABC, abstractmethod
from datetime import datetime

# Clase abstracta
class Participante(ABC):
    def __init__(self, identificacion, nombre_completo, genero, tecnica_artistica, numero_clases, costo_por_clase):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.genero = genero
        self.tecnica_artistica = tecnica_artistica
        self.numero_clases = numero_clases
        self.costo_por_clase = costo_por_clase

    @abstractmethod
    def calcular_costo_total(self):
        pass

# Clase concreta que hereda Participante
class GestionParticipantes(Participante):
    def __init__(self, identificacion, nombre_completo, genero, tecnica_artistica, numero_clases, costo_por_clase):
        super().__init__(identificacion, nombre_completo, genero, tecnica_artistica, numero_clases, costo_por_clase)
        self.fecha_registro = datetime.now()

    def calcular_costo_total(self):
        return self.numero_clases * self.costo_por_clase

    def mostrar_reporte(self):
        total = self.calcular_costo_total()
        reporte = (
            f"ID: {self.identificacion}\n"
            f"Nombre: {self.nombre_completo}\n"
            f"Género: {self.genero}\n"
            f"Técnica artística: {self.tecnica_artistica}\n"
            f"Número de clases: {self.numero_clases}\n"
            f"Costo por clase: ${self.costo_por_clase}\n"
            f"Total a pagar: ${total}\n"
            f"Fecha de registro: {self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        return reporte

# Diccionario con los costos por técnica artística
COSTOS = {
    "Dibujo": 70000,
    "Pintura": 85000,
    "Escritura": 100000,
    "Fotografía": 90000,
    "Grabado": 75000
}

# Ventana de acceso
class VentanaAcceso(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("220x160")
        self.resizable(False, False)

        tk.Label(self, text="Aplicacion: Gestion de Participantes").pack(pady=5)
        tk.Label(self, text="Autor: Harvin Eduardo Rojas Flórez").pack(pady=5)
        tk.Label(self, text="Ingrese la contraseña:").pack(pady=5)
        self.pass_var = tk.StringVar()
        self.entry_pass = tk.Entry(self, textvariable=self.pass_var, show="*")
        self.entry_pass.pack(pady=5)
        self.entry_pass.focus()

        tk.Button(self, text="Ingresar", command=self.verificar_contrasena).pack(pady=10)

    def verificar_contrasena(self):
        if self.pass_var.get() == "123":
            self.destroy()
            app = Aplicacion()
            app.mainloop()
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
            self.pass_var.set("")
            self.entry_pass.focus()

# Interfaz principal
class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Participantes - Academia Melodías Perfectas")
        self.geometry("450x450")

        # Variables del formulario
        self.identificacion = tk.StringVar()
        self.nombre_completo = tk.StringVar()
        self.genero = tk.StringVar(value="Masculino")
        self.tecnica_artistica = tk.StringVar()
        self.numero_clases = tk.StringVar()
        self.costo_por_clase = tk.StringVar()

        # Participante guardado (inicialmente ninguno)
        self.participante = None
        self.registro = []

        # Construcción de widgets
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="ID:").pack(anchor="w", padx=10, pady=2)
        tk.Entry(self, textvariable=self.identificacion, width=20).pack(padx=10, anchor="w")

        tk.Label(self, text="Nombre completo:").pack(anchor="w", padx=10, pady=2)
        tk.Entry(self, textvariable=self.nombre_completo,width=40).pack(padx=10, anchor="w")

        tk.Label(self, text="Género:").pack(anchor="w", padx=10, pady=2)
        frame_genero = tk.Frame(self)
        frame_genero.pack(anchor="w", padx=10)
        tk.Radiobutton(frame_genero, text="Masculino", variable=self.genero, value="Masculino").pack(side="left")
        tk.Radiobutton(frame_genero, text="Femenino", variable=self.genero, value="Femenino").pack(side="left")

        tk.Label(self, text="Técnica artística:").pack(anchor="w", padx=10, pady=2)
        frame_tecnica = tk.Frame(self)
        frame_tecnica.pack(anchor="w", padx=10)

        self.combo_tecnica = ttk.Combobox(frame_tecnica, textvariable=self.tecnica_artistica, state="readonly", width=27)
        self.combo_tecnica['values'] = list(COSTOS.keys())
        self.combo_tecnica.pack()
        self.combo_tecnica.bind("<<ComboboxSelected>>", lambda event: self.actualizar_costo(self.tecnica_artistica.get()))

        tk.Label(self, text="Número de clases:").pack(anchor="w", padx=10, pady=2)
        tk.Entry(self, textvariable=self.numero_clases, width=20).pack(padx=10, anchor="w")

        tk.Label(self, text="Costo por clase:").pack(anchor="w", padx=10, pady=2)
        self.entry_costo = tk.Entry(self, textvariable=self.costo_por_clase, state="readonly",width=40)
        self.entry_costo.pack(padx=10, anchor="center")

        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=15)

        tk.Button(frame_botones, text="Calcular / Mostrar Reporte", command=self.calcular_y_mostrar, width=25).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(frame_botones, text="Guardar Registro", command=self.guardar_registro, width=20).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(frame_botones, text="Ver Todos los Registros", command=self.mostrar_todos_los_registros, width=25).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame_botones, text="Salir", command=self.confirmar_salida, width=20).grid(row=1, column=1, padx=5, pady=5)

    def actualizar_costo(self, seleccion):
        costo = COSTOS.get(seleccion, 0)
        self.costo_por_clase.set(str(costo))

    def calcular_y_mostrar(self):
        # Validar campos
        try:
            identificacion = int(self.identificacion.get())
            nombre = self.nombre_completo.get().strip()
            genero = self.genero.get()
            tecnica = self.tecnica_artistica.get()
            numero_clases = int(self.numero_clases.get())
            costo_clase = int(self.costo_por_clase.get())

            if not nombre or not tecnica:
                messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")
                return

            # Crear objeto temporal para mostrar reporte
            participante_temp = GestionParticipantes(
                identificacion, nombre, genero, tecnica, numero_clases, costo_clase
            )

            # Mostrar reporte en ventana nueva
            self.mostrar_ventana_reporte(participante_temp)

        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, ingrese valores numéricos válidos para ID y número de clases.")
    
    def limpiar_campos(self):
            self.identificacion.set("")
            self.nombre_completo.set("")
            self.genero.set("Masculino")  
            self.tecnica_artistica.set("")
            self.numero_clases.set("")
            self.costo_por_clase.set("")

    def guardar_registro(self):
        try:
            identificacion = int(self.identificacion.get())
            nombre = self.nombre_completo.get().strip()
            genero = self.genero.get()
            tecnica = self.tecnica_artistica.get()
            numero_clases = int(self.numero_clases.get())
            costo_clase = int(self.costo_por_clase.get())

            if not nombre or not tecnica:
                messagebox.showwarning("Datos incompletos", "Por favor, complete todos los campos.")
                return

            self.participante = GestionParticipantes(
                identificacion, nombre, genero, tecnica, numero_clases, costo_clase
            )
            self.registro.append(self.participante)
            messagebox.showinfo("Registro guardado", "Datos del participante guardados correctamente.")
            self.limpiar_campos()
        except ValueError:
            messagebox.showerror("Error de entrada", "Por favor, ingrese valores numéricos válidos para ID y número de clases.")

    def mostrar_ventana_reporte(self, participante):
        ventana_reporte = tk.Toplevel(self)
        ventana_reporte.title("Reporte del Participante")
        ventana_reporte.geometry("400x350")

        datos = participante.mostrar_reporte().split('\n')

        for dato in datos:
            tk.Label(ventana_reporte, text=dato, anchor="w", justify="left").pack(fill="x", padx=20, pady=5)

        tk.Button(ventana_reporte, text="Cerrar", command=ventana_reporte.destroy).pack(pady=10)

    def mostrar_todos_los_registros(self):
        if not self.registro:
            messagebox.showinfo("Sin registros", "No hay participantes registrados aún.")
            return

        ventana_todos = tk.Toplevel(self)
        ventana_todos.title("Todos los Registros de Participantes")
        ventana_todos.geometry("500x500")

        # Usamos un widget Text para mostrar todo el contenido con scroll
        text_area = tk.Text(ventana_todos, wrap="word")
        text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Añadir scroll
        scroll = tk.Scrollbar(ventana_todos, command=text_area.yview)
        scroll.pack(side="right", fill="y")
        text_area.config(yscrollcommand=scroll.set)

        # Mostrar todos los reportes
        for idx, participante in enumerate(self.registro, start=1):
            text_area.insert("end", f"--- Participante #{idx} ---\n")
            text_area.insert("end", participante.mostrar_reporte())
            text_area.insert("end", "\n" + "-"*50 + "\n\n")

        text_area.config(state="disabled")  # Hacer el texto solo de lectura

        # Mostrar todos los reportes
        for idx, participante in enumerate(self.registro, start=1):
            text_area.insert("end", f"--- Participante #{idx} ---\n")
            text_area.insert("end", participante.mostrar_reporte())
            text_area.insert("end", "\n" + "-"*50 + "\n\n")

        text_area.config(state="disabled")  # Hacer el texto solo de lectura

    def confirmar_salida(self):
        if messagebox.askyesno("Salir", "¿Está seguro que desea salir?"):
            self.destroy()

if __name__ == "__main__":
    ventana_acceso = VentanaAcceso()
    ventana_acceso.mainloop()
