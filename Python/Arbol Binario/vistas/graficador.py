class GraficadorArbol:

    def __init__(self, canvas):
        self.canvas = canvas

    def limpiar(self):
        self.canvas.delete("all")

    def dibujar_arbol(self, raiz):
        self.limpiar()
        if raiz:
            self._dibujar_nodo(raiz, 400, 30, 150)

    def _dibujar_nodo(self, nodo, x, y, dx):
        if nodo is None:
            return

        radio = 20
        self.canvas.create_oval(x-radio, y-radio, x+radio, y+radio, fill="lightblue")
        self.canvas.create_text(x, y, text=str(nodo.valor), font=("Arial", 12, "bold"))

        if nodo.izq:
            self.canvas.create_line(x, y+20, x-dx, y+70-20, arrow="last")
            self._dibujar_nodo(nodo.izq, x-dx, y+70, dx/2)

        if nodo.der:
            self.canvas.create_line(x, y+20, x+dx, y+70-20, arrow="last")
            self._dibujar_nodo(nodo.der, x+dx, y+70, dx/2)

    def dibujar_recorrido(self, canvas, lista):
        canvas.delete("all")  

        # Variables para el dibujo en el canvas
        x_start = 20  # Posición inicial en X
        y_start = 10  # Posición inicial en Y
        space = 30    # Espacio entre cada nodo en X
        line_height = 30  # Espacio entre filas en Y
        max_elements_per_row = 8  # Número máximo de elementos por fila

        x = x_start
        y = y_start
        count = 0  # Contador de elementos por fila

        # Dibujar cada elemento
        for v in lista:
           #canvas.create_oval(x-15, y-15, x+15, y+15, fill="lightgreen")  # Dibuja el nodo
            canvas.create_text(x, y, text=str(v), font=("Arial", 12, "bold"))  # El texto del valor

            
            x += space
            count += 1

            # Si alcanzamos el máximo de elementos en una fila, pasamos a la siguiente línea
            if count >= max_elements_per_row:
                count = 0
                x = x_start  # Volver a la posición inicial en X
                y += line_height  # Mover hacia abajo una línea
