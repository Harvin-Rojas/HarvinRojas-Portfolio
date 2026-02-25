import tkinter as tk
from tkinter import ttk, messagebox
from collections import deque
from datetime import datetime
from tkcalendar import DateEntry
from tkinter import simpledialog


class Usuario:
    def __init__(self, tipo_id, num_id, nombre, edad, estrato, tipo_atencion, copago, fecha):
        self.tipo_id = tipo_id
        self.num_id = num_id
        self.nombre = nombre
        self.edad = edad
        self.estrato = estrato
        self.tipo_atencion = tipo_atencion
        self.copago = copago
        self.fecha = fecha

class EstructuraDatosUsuario:
    def __init__(self):
        self.pila = []        
        self.cola = deque()   
        self.lista = []       

    # Registrar usuario según la estructura
    def registrar(self, usuario, estructura):
        if estructura == "Pila":
            self.pila.append(usuario)
        elif estructura == "Cola":
            self.cola.append(usuario)
        elif estructura == "Lista":
            self.lista.append(usuario)

    # Eliminar usuario según la estructura
    def eliminar(self, estructura, num_id=None):
        if estructura == "Pila" and self.pila:
            return self.pila.pop()
        elif estructura == "Cola" and self.cola:
            return self.cola.popleft()
        elif estructura == "Lista" and num_id:
            for u in self.lista:
                if u.num_id == num_id:
                    self.lista.remove(u)
                    return u
        return None

    # Reporte según estructura
    def reporte(self, estructura):
        if estructura == "Pila":
            return sum(u.copago for u in self.pila)
        elif estructura == "Cola":
            return len(self.cola)
        elif estructura == "Lista":
            if self.lista:
                return sum(u.edad for u in self.lista) / len(self.lista)
            return 0

class EPSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - EPS Salvando Vidas")
        self.root.geometry("350x200")
        self.datos = EstructuraDatosUsuario()

        
     
        self.login_screen()


    def login_screen(self):
        self.clear_window()
        acerca_label = tk.Label(self.root, text="Acerca de", fg="#535353", cursor="hand2", font=("Arial", 10, "underline"))
        acerca_label.pack(anchor="w", padx=30, pady=(0, 10)) 
        acerca_label.bind("<Button-1>", lambda e: self.acerca_de())
        
        tk.Label(self.root, text="Contraseña:", font=("Arial", 12)).pack(pady=20)
        
        
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)
        
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5) 

        tk.Button(button_frame, text="Ingresar", command=self.validar_login).pack(side="left", padx=5)
        tk.Button(button_frame, text="Salir", command=self.root.destroy).pack(side="left", padx=5)
  
    def validar_login(self):
        if self.password_entry.get().strip() == "unad":
            self.formulario_usuarios()    
        else:
            messagebox.showerror("Error", "Contraseña incorrecta")
            self.password_entry.delete(0, tk.END)           
            

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "EPS Salvando Vidas\nDesarrollo de aplicacion - Python Tkinter\nEstudiante: Harvin Eduardo Rojas Flórez\nGrupo: 72")


    def formulario_usuarios(self):
        self.clear_window()
        self.root.title("EPS Salvando Vidas  Control de Usuarios")
        self.root.state("zoomed")  
        
        
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=10, padx=10, fill="x")
        
        frame_form = tk.LabelFrame(self.root, text="Registro de Usuarios", padx=10, pady=10, font=("Arial", 10, "bold"))
        frame_form.pack(padx=20, pady=10, fill="x")
        
        tk.Label(frame_form, text="Estructura:").grid(row=0, column=0, sticky="w", pady=2)
        self.estructura_usuario_cb = ttk.Combobox(frame_form, values=["Pila","Cola","Lista"], width=25)
        self.estructura_usuario_cb.grid(row=0, column=1, sticky="w")
        self.estructura_usuario_cb.bind("<<ComboboxSelected>>", self.mostrar_treeview)
        
        tk.Label(frame_form, text="Tipo ID:").grid(row=1, column=0, sticky="w", pady=2)
        self.tipo_id_cb = ttk.Combobox(frame_form, values=["CC", "CE", "NUIP", "PAS"], width=25)
        self.tipo_id_cb.grid(row=1, column=1, pady=2, sticky="w")

        tk.Label(frame_form, text="Número ID:").grid(row=2, column=0, sticky="w", pady=2)
        self.num_id_entry = tk.Entry(frame_form, width=28)
        self.num_id_entry.grid(row=2, column=1, pady=2, sticky="w")

        tk.Label(frame_form, text="Nombre:").grid(row=3, column=0, sticky="w", pady=2)
        self.nombre_entry = tk.Entry(frame_form, width=28)
        self.nombre_entry.grid(row=3, column=1, pady=2, sticky="w")

        tk.Label(frame_form, text="Edad:").grid(row=4, column=0, sticky="w", pady=2)
        self.edad_entry = tk.Entry(frame_form, width=28)
        self.edad_entry.grid(row=4, column=1, pady=2, sticky="w")

        tk.Label(frame_form, text="Estrato:").grid(row=5, column=0, sticky="w", pady=2)
        self.estrato_cb = ttk.Combobox(frame_form, values=[1,2,3,4,5,6], width=25)
        self.estrato_cb.grid(row=5, column=1, pady=2, sticky="w")

        tk.Label(frame_form, text="Atención:").grid(row=6, column=0, sticky="w", pady=2)
        self.tipo_atencion_var = tk.StringVar()
        tk.Radiobutton(frame_form, text="Medicina general", variable=self.tipo_atencion_var, value="Medicina general", command=self.calcular_copago).grid(row=6, column=1, sticky="w")
        tk.Radiobutton(frame_form, text="Examen laboratorio", variable=self.tipo_atencion_var, value="Examen laboratorio", command=self.calcular_copago).grid(row=6, column=2, sticky="w")

        tk.Label(frame_form, text="Fecha Registro:").grid(row=7, column=0, sticky="w", pady=2)
        self.fecha_var = tk.StringVar()
        self.fecha_var.set(datetime.today().strftime("%d/%m/%Y"))  
        self.fecha_entry = tk.Entry(frame_form, textvariable=self.fecha_var, state="readonly", width=28)
        self.fecha_entry.grid(row=7, column=1, sticky="w", pady=2)

        tk.Label(frame_form, text="Copago:").grid(row=8, column=0, sticky="w", pady=2)
        self.copago_var = tk.DoubleVar()
        tk.Entry(frame_form, textvariable=self.copago_var, state="readonly", width=28).grid(row=8, column=1, pady=2, sticky="w")
        
        button_frame = tk.Frame(frame_form)
        button_frame.grid(row=9, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="Registrar", command=self.registrar_usuario).pack(side="left", padx=5)
        tk.Button(button_frame, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)
       

       
        
        
        frame_tabla = tk.LabelFrame(self.root, text="Datos de Usuarios", padx=5, pady=5, relief="groove", bd=2, font=("Arial", 10, "bold"))
        frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

        tk.Label(frame_tabla, text="Ver Estructura:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
        self.estructura_cb = ttk.Combobox(frame_tabla, values=["Pila","Cola","Lista"], state="readonly", width=25)
        self.estructura_cb.grid(row=0, column=0, sticky="w", padx=100, pady=2)
        self.estructura_cb.bind("<<ComboboxSelected>>", self.mostrar_treeview)

         
        
        reporte_frame = tk.Frame(self.root)
        reporte_frame.pack(anchor="w", padx=30, pady=(10, 0))
        

        button_frame_reportes = tk.Frame(self.root)
        button_frame_reportes.pack(fill="x", padx=30, pady=(5, 10))

       
        button_frame_reportes.columnconfigure(0, weight=1) 
        button_frame_reportes.columnconfigure(1, weight=0)  

        
        tk.Button(button_frame_reportes, text="Reporte", width=8, command=self.generar_reporte).grid(row=0, column=0, sticky="w", padx=5)
        tk.Button(button_frame_reportes, text="Eliminar", width=8, command=self.eliminar_usuario).grid(row=0, column=0, sticky="w", padx=80)
        tk.Button(button_frame_reportes, text="Salir", width=8, command=self.root.destroy).grid(row=0, column=1, sticky="e", padx=5)
    
        
        
       
        self.treeframes = {}
        self.trees = {}
        for estructura in ["Pila","Cola","Lista"]:
            frame = tk.Frame(frame_tabla, relief="groove", bd=2)
            columns = ("Estructura","ID","Nombre","Edad","Estrato","Atención","Copago","Fecha")
            tree = ttk.Treeview(frame, columns=columns, show="headings", height=5)
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=160, anchor="center")
            tree.pack(fill="both", expand=True)
            frame.grid(row=1, column=0, pady=10, sticky="ew")
            frame.pack_forget()  # se oculta al inicio
            self.treeframes[estructura] = frame
            self.trees[estructura] = tree

  
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_treeview(self, event=None):
        estructura = self.estructura_cb.get()
        if not estructura:
            return

        # Ocultar todas
        for f in self.treeframes.values():
            f.grid_remove()

        # Mostrar la seleccionada
        frame = self.treeframes[estructura]
        frame.grid(row=1, column=0, pady=10, sticky="nsew")  

        self.actualizar_treeview(estructura)




    def calcular_copago(self):
        estrato = self.estrato_cb.get()
        tipo_atencion = self.tipo_atencion_var.get()

        if not estrato or not tipo_atencion:
            self.copago_var.set(0)
            return

        estrato = int(estrato)

        if tipo_atencion == "Medicina general":
            copago_dict = {1:0, 2:0, 3:10000, 4:15000, 5:20000, 6:30000}
        else:  
            copago_dict = {1:0, 2:0, 3:0, 4:5000, 5:10000, 6:20000}

        self.copago_var.set(copago_dict.get(estrato, 0))

    def registrar_usuario(self):
    
        if not all([
            self.tipo_id_cb.get(),
            self.num_id_entry.get(),
            self.nombre_entry.get(),
            self.edad_entry.get(),
            self.estrato_cb.get(),
            self.tipo_atencion_var.get(),
            self.estructura_usuario_cb.get()
        ]):
            messagebox.showerror("Error", "Complete todos los campos obligatorios")
            return

    
        try:
            num_id = int(self.num_id_entry.get())
            edad = int(self.edad_entry.get())
        except ValueError:
            messagebox.showerror("Error", "ID Y EDAD deben ser numéricos")
            return

        
        fecha = self.fecha_var.get()

    
        estrato = int(self.estrato_cb.get())
        tipo_atencion = self.tipo_atencion_var.get()

        if tipo_atencion == "Medicina general":
            copago_dict = {1:0, 2:0, 3:10000, 4:15000, 5:20000, 6:30000}
        else:  
            copago_dict = {1:0, 2:0, 3:0, 4:5000, 5:10000, 6:20000}

        copago = copago_dict.get(estrato, 0)

        usuario = Usuario(
            tipo_id=self.tipo_id_cb.get(),
            num_id=num_id,
            nombre=self.nombre_entry.get(),
            edad=edad,
            estrato=estrato,
            tipo_atencion=tipo_atencion,
            copago=copago,
            fecha=fecha
        )

        estructura = self.estructura_usuario_cb.get().strip().capitalize()
        if estructura not in ["Pila","Cola","Lista"]:
            messagebox.showerror("Error", "Seleccione una estructura válida")
            return

        self.datos.registrar(usuario, estructura)  
        self.actualizar_treeview(estructura)     

        self.actualizar_treeview(estructura)

        messagebox.showinfo("Éxito", f"Usuario registrado en {estructura}")
    


    def actualizar_treeview(self, estructura):
        tree = self.trees[estructura]
        tree.delete(*tree.get_children())
        data = getattr(self.datos, estructura.lower())
        for u in data:
           tree.insert("", "end", values=(estructura, u.num_id, u.nombre, u.edad, u.estrato, u.tipo_atencion, u.copago, u.fecha))

    def generar_reporte(self):
        estructura = self.estructura_cb.get()
        if not estructura:
            messagebox.showwarning("Atención", "Seleccione una estructura para generar el reporte.")
            return

        resultado = self.datos.reporte(estructura)

        # Crear ventana flotante
        ventana_reporte = tk.Toplevel(self.root)
        ventana_reporte.title(f"Reporte de {estructura}")
        ventana_reporte.geometry("400x200")
        ventana_reporte.transient(self.root)  # hace que la ventana esté sobre la principal
        ventana_reporte.grab_set()  # bloquea interacción con la ventana principal

        tk.Label(ventana_reporte, text=f"Reporte de {estructura}", font=("Arial", 14, "bold")).pack(pady=10)

        if estructura == "Pila":
            texto = f"Suma total de copagos: ${resultado:,.0f}"
        elif estructura == "Cola":
            texto = f"Cantidad de registros: {resultado}"
        elif estructura == "Lista":
            texto = f"Promedio de edad: {resultado:.2f} años"

        tk.Label(ventana_reporte, text=texto, font=("Arial", 12)).pack(pady=10)

        tk.Button(ventana_reporte, text="Cerrar", command=ventana_reporte.destroy).pack(pady=10)
            
    def eliminar_usuario(self):
        estructura = self.estructura_cb.get()
        if not estructura:
            messagebox.showwarning("Atención", "Seleccione una estructura para eliminar.")
            return

        if estructura == "Lista":
            
            num_id = simpledialog.askinteger("Eliminar de Lista", "Digite el número de identificación del usuario a eliminar:")
            if num_id is None:
                return
            confirmar = messagebox.askyesno("Confirmar", f"¿Eliminar usuario con ID {num_id}?")
            if confirmar:
                eliminado = self.datos.eliminar("Lista", num_id)
                if eliminado:
                    messagebox.showinfo("Eliminado", f"Usuario {eliminado.nombre} eliminado de la Lista.")
                else:
                    messagebox.showerror("Error", "No se encontró el usuario en la Lista.")
        else:
            
            confirmar = messagebox.askyesno("Confirmar", f"¿Desea eliminar un registro de {estructura}?")
            if confirmar:
                eliminado = self.datos.eliminar(estructura)
                if eliminado:
                    messagebox.showinfo("Eliminado", f"Usuario {eliminado.nombre} eliminado de {estructura}.")
                else:
                    messagebox.showwarning("Atención", f"No hay registros en {estructura}.")

        self.actualizar_treeview(estructura)


    def limpiar_campos(self):
        self.tipo_id_cb.set("")
        self.num_id_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.edad_entry.delete(0, tk.END)
        self.estrato_cb.set("")
        self.tipo_atencion_var.set("")
        self.fecha_var.set(datetime.today().strftime("%d/%m/%Y"))
        self.copago_var.set(0)
        self.estructura_cb.set("")


if __name__ == "__main__":
    root = tk.Tk()
    app = EPSApp(root)
    root.mainloop()
