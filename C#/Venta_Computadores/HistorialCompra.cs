namespace Venta_Computadores
{
   class HistorialCompra
   {
        public List<Producto> Productos { get; set; }
        public DateTime FechaCompra { get; set; }
        public decimal Total { get; set; }  // Agregamos un campo para el total

        // Constructor actualizado para aceptar ambos argumentos: productos y total
        public HistorialCompra(List<Producto> productos, decimal total)
        {
            Productos = productos;
            FechaCompra = DateTime.Now;
            Total = total;  // Almacenamos el total de la compra
        }

        public override string ToString()
        {
            var productosStr = string.Join(", ", Productos.Select(p => p.nombre));
            return $"Fecha: {FechaCompra}, Productos: {productosStr}, Total: {Total:C}";
        }
    }
}