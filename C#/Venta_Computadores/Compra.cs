namespace Venta_Computadores
{
    class Compra
    {
        public Usuario Usuario { get; set; }
        public List<Producto> Productos { get; set; }
        public DateTime FechaCompra { get; set; }
        public decimal Total { get; set; }  // Nuevo campo para almacenar el total de la compra

        public Compra(Usuario usuario, List<Producto> productos, DateTime fechaCompra, decimal total)
        {
            Usuario = usuario;
            Productos = productos;
            FechaCompra = fechaCompra;
            Total = total;
        }

        public override string ToString()
        {
            var productosStr = string.Join(", ", Productos.Select(p => p.nombre));
            return $"Fecha: {FechaCompra}, Productos: {productosStr}, Total: {Total:C}";
        }
    }
}
